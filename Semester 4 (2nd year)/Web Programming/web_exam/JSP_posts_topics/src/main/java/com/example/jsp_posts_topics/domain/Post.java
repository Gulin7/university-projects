package com.example.jsp_posts_topics.domain;

public class Post {
    private int id;
    private String user;
    private int topicId;
    private String text;
    private int date;

    public Post(int id, String user, int topicId, String text, int date) {
        this.id = id;
        this.user = user;
        this.topicId = topicId;
        this.text = text;
        this.date = date;
    }

    public int getId() {
        return id;
    }
    public String getUser() {
        return user;
    }
    public int getTopicId() {
        return topicId;
    }
    public String getText() {
        return text;
    }
    public int getDate() {
        return date;
    }
    public void setId(int id) {
        this.id = id;
    }
    public void setUser(String user) {
        this.user = user;
    }
    public void setTopicId(int topicId) {
        this.topicId = topicId;
    }
    public void setText(String text) {
        this.text = text;
    }
    public void setDate(int date) {
        this.date = date;
    }
    @Override
    public String toString() {
        return "";
    }
}
