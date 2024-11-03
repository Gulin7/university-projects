package com.example.jsp1.model;

public class Topic {
    private int id;
    private String topicname;

    public Topic(int id, String topicname) {
        this.id = id;
        this.topicname = topicname;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTopicname() {
        return topicname;
    }

    public void setTopicname(String topicname) {
        this.topicname = topicname;
    }
}
