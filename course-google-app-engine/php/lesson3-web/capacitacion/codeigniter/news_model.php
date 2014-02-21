<?php

class News_model extends CI_Model {

    public function __construct() {
    	$this->load->library('session');
    	if ($this->session->userdata('news') == NULL) {
    		$this->session->set_userdata('news', array());
    	}
    }

    public function get_news($slug = FALSE) {
        if ($slug === FALSE) {
            return $this->session->userdata('news');
        } else {
        	$news = $this->session->userdata('news');
        	return $news[$slug];
        }
    }

    public function set_news() {
        $this->load->helper('url');

        $slug = url_title($this->input->post('title'), 'dash', TRUE);

        $data = array(
            'title' => $this->input->post('title'),
            'slug' => $slug,
            'text' => $this->input->post('text')
        );

		$news = $this->session->userdata('news');
		$news[$slug] = $data;
        $this->session->set_userdata('news', $news);
    }

}