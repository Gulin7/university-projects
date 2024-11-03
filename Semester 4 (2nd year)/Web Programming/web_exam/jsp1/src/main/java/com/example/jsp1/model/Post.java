package com.example.jsp1.model;

public class Post {
    private int id;
    private String user;
    private int topicid;
    private String text;
    private int date;

    public Post(int id, String user, int topicid, String text, int date) {
        this.id = id;
        this.user = user;
        this.topicid = topicid;
        this.text = text;
        this.date = date;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public int getTopicid() {
        return topicid;
    }

    public void setTopicid(int topicid) {
        this.topicid = topicid;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        this.date = date;
    }
}
