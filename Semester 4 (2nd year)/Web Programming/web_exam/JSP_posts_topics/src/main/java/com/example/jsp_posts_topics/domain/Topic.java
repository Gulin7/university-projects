package com.example.jsp_posts_topics.domain;

public class Topic {
    private final int id;
    private final String topicName;

    public Topic(int id, String topicName) {
        this.id = id;
        this.topicName = topicName;
    }

    public int getId() {
        return id;
    }

    public String getTopicName() {
        return topicName;
    }

    public String toString() {
        return "Topic{" +
                "id=" + id +
                ", topic name:" + topicName + '\'' +
                '}';
    }
}
