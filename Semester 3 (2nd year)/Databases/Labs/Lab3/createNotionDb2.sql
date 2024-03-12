use NotionDabatase;


create table areas
(
area_id         int not null,
constraint pk_areas  primary key(area_id),
name        varchar(50) not null,
archive     bit not null,
description varchar(max),
)

create table projects
(
project_id         int not null,
constraint pk_projects  primary key(project_id),
title       varchar(50) not null,
archive     bit not null,
area_id         int not null,
constraint fk_area foreign key(area_id) references areas(area_id),
status      bit not null,
description varchar(max),
)

create table resources (
resource_id         int not null,
constraint pk_resources  primary key(resource_id),
name        varchar(50) not null,
archive     bit not null,
description varchar(max),
project_id         int not null,
constraint fk_projects foreign key(project_id) references projects(project_id),
)

create table authors
(
author_id   int not null,
constraint pk_authors primary key(author_id),
full_name varchar(50) not null,
username  varchar(50) not null,
email     varchar(30) not null,
role      varchar(30) not null,
salary    int not null,
password  varchar(100) not null,
project_id       int null,
constraint fk_project_id foreign key (project_id) references projects(project_id),
bio       varchar(max),
)

create table tasks (
task_id int not null,
constraint pk_tasks  primary key(task_id),
name varchar(50) not null,
due date,
project_id int not null,
constraint fk_project foreign key(project_id) references projects(project_id),
author_id int null,
constraint fk_author_id foreign key (author_id) references authors(author_id),
status bit not null,
)

create table notes (
note_id       int not null,
constraint pk_notes  primary key(note_id),
title         varchar(50) not null,
tags          varchar(50) not null,
archive       bit not null,
creation_date date not null,
resource_id   int not null,
constraint fk_resource_id foreign key (resource_id) references resources(resource_id),
content       varchar(max),
)

create table images (
image_id int not null,
constraint pk_images  primary key(image_id),
title varchar(50) not null,
type varchar(50) not null,
creator varchar(50) not null,
height int not null,
width int not null,
format varchar(25) not null,
)

create table videos (
video_id         int not null,
constraint pk_videos  primary key(video_id),
title       varchar(50) not null,
type        varchar(50) not null,
description varchar(max),
size        int not null,
creator     varchar(50) not null,
duration    time(7) not null,
format      varchar(25) not null,
)

create table audios (
audio_id    int not null,
constraint pk_audios  primary key(audio_id),
title       varchar(50) not null,
type        varchar(50) not null,
description varchar(max),
size        int not null,
creator     varchar(50) not null,
duration    time(7) not null,
format      varchar(25) not null,
)

create table webclips (
webclip_id int not null,
constraint pk_webclips  primary key(webclip_id),
title varchar(50) not null,
link varchar(100) unique not null,
)

create table authors_notes (
note_id int not null,
constraint fk_authors_notes_notes foreign key(note_id) references notes(note_id),
author_id int not null,
constraint fk_authors_notes_authors foreign key(author_id) references authors(author_id),
constraint pk_authors_notes  primary key(note_id,author_id),
)

create table images_notes (
note_id int not null,
constraint fk_images_notes_notes foreign key(note_id) references notes(note_id),
image_id int not null,
constraint fk_images_notes_images foreign key(image_id) references images(image_id),
constraint pk_images_notes primary key(note_id,image_id),
)

create table audios_notes (
note_id int not null,
constraint fk_audios_notes_notes foreign key(note_id) references notes(note_id),
audio_id int not null,
constraint fk_audios_notes_audios foreign key(audio_id) references audios(audio_id),
constraint pk_audios_notes primary key(note_id,audio_id),
)

create table webclips_notes (
note_id int not null,
constraint fk_webclips_notes_notes foreign key(note_id) references notes(note_id),
webclip_id int not null,
constraint fk_webclips_notes_webclips foreign key(webclip_id) references webclips(webclip_id),
constraint pk_webclips_notes primary key(note_id,webclip_id),
)

create table videos_notes (
note_id int not null,
constraint fk_videos_notes_notes foreign key(note_id) references notes(note_id),
video_id int not null,
constraint fk_videos_notes_videos foreign key(video_id) references videos(video_id),
constraint pk_videos_notes primary key(note_id,video_id),
)