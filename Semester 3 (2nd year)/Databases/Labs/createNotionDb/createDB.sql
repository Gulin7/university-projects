use NotionDb;
GO


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
    -- Insert data into the 'areas' table
    INSERT INTO areas (area_id, name, archive, description)
    VALUES
        (1,'Web Development', 0, 'Projects related to web development and frontend technologies.'),
        (2,'Mobile App Development', 0, 'Projects focused on mobile application development.'),
        (3,'Data Analytics', 0, 'Projects involving data analysis and analytics.');

    -- Insert data into the 'projects' table with references to areas
    INSERT INTO projects (project_id, title, archive, area_id, status, description)
    VALUES
        (1, 'E-commerce Website Redesign', 0, 1, 1, 'Redesign and modernize the user interface and functionality of our e-commerce website to enhance the user experience and boost sales.'),
        (2, 'Mobile App Development: Task Manager', 0, 2, 1, 'Develop a cross-platform mobile app for task management that allows users to create, assign, and track tasks, improving team productivity.'),
        (3, 'Financial Analytics Dashboard', 0, 3, 1, 'Create an analytics dashboard for financial data to help businesses make data-driven decisions and gain insights into their financial performance.');

    -- Insert 10 authors for the first project (project_id = 1)
    INSERT INTO authors (author_id, full_name, username, email, role, password, bio, project_id, salary)
    VALUES
        (1, 'Alice Smith', 'alicesmith', 'alicesmith@email.com', 'Software Developer', 'P@ssw0rd1', 'Experienced software developer with a passion for creating efficient and elegant code. Proficient in various programming languages and frameworks.', 1, 5000),
        (2, 'Daniel Johnson', 'danieljohnson', 'danieljohnson@email.com', 'Quality Assurance Engineer', 'P@ssw0rd2', 'Detail-oriented QA engineer with a focus on ensuring software quality and reliability. Experienced in manual and automated testing.', 1, 3500),
        (3, 'Olivia Brown', 'oliviabrown', 'oliviabrown@email.com', 'Frontend Developer', 'P@ssw0rd3', 'Frontend developer with a knack for crafting stunning user interfaces. Skilled in HTML, CSS, and JavaScript.', 1, 7000),
        (4, 'William Davis', 'williamdavis', 'williamdavis@email.com', 'Backend Developer', 'P@ssw0rd4', 'Backend developer specializing in building scalable and performant server-side applications. Proficient in database design and optimization.', 1, 8000),
        (5,'Sophia Wilson', 'sophiawilson', 'sophiawilson@email.com', 'UI/UX Designer', 'P@ssw0rd5', 'UI/UX designer focused on creating intuitive and visually appealing user experiences. Proficient in design tools and user research.', 1, 2000),
        (6, 'James Martin', 'jamesmartin', 'jamesmartin@email.com', 'Scrum Master', 'P@ssw0rd6', 'Certified Scrum Master with a track record of facilitating agile development processes. Skilled in team collaboration and Agile methodologies.', 1, 3800),
        (7, 'Ava Taylor', 'avataylor', 'avataylor@email.com', 'DevOps Engineer', 'P@ssw0rd7', 'DevOps engineer with expertise in automation, continuous integration, and deployment. Dedicated to optimizing software delivery processes.', 1, 12000),
        (8, 'Logan Clark', 'loganclark', 'loganclark@email.com', 'Database Administrator', 'P@ssw0rd8', 'Database administrator responsible for managing and optimizing databases to ensure data integrity and performance.', 1, 4500),
        (9, 'Mia Lewis', 'mialewis', 'mialewis@email.com', 'Full Stack Developer', 'P@ssw0rd9', 'Full stack developer proficient in both frontend and backend technologies. Enjoys creating end-to-end solutions.', 1, 5600),
        (10, 'Benjamin Moore', 'benjaminmoore', 'benjaminmoore@email.com', 'System Architect', 'P@ssw0rd10', 'System architect focused on designing scalable and robust software architectures. Experienced in system integration and performance optimization.', 1, 2300);

    -- Insert 10 authors for the second project (project_id = 2)
    INSERT INTO authors (author_id, full_name, username, email, role, password, bio, project_id, salary)
    VALUES
        (11, 'Ella Taylor', 'ellataylor', 'ellataylor@email.com', 'Product Owner', 'P@ssw0rd11', 'Product owner responsible for defining product features and prioritizing development efforts. Skilled in product strategy and customer feedback analysis.', 2, 3450),
        (12, 'Henry Turner', 'henryturner', 'henryturner@email.com', 'Mobile App Developer', 'P@ssw0rd12', 'Mobile app developer specializing in Android and iOS app development. Enthusiastic about creating mobile solutions.', 2, 1250),
        (13, 'Sofia Scott', 'sofiascott', 'sofiascott@email.com', 'Data Scientist', 'P@ssw0rd13', 'Data scientist with expertise in data analysis and machine learning. Passionate about extracting insights from data.', 2, 2450),
        (14, 'Jackson Allen', 'jacksonallen', 'jacksonallen@email.com', 'Network Engineer', 'P@ssw0rd14', 'Network engineer responsible for designing and maintaining network infrastructure. Proficient in network security and protocols.', 2, 4000),
        (15, 'Avery Hall', 'averyhall', 'averyhall@email.com', 'Test Automation Engineer', 'P@ssw0rd15', 'Test automation engineer with a focus on creating automated testing solutions for software quality assurance.', 2, 2500),
        (16, 'Scarlett King', 'scarlettking', 'scarlettking@email.com', 'Cloud Solutions Architect', 'P@ssw0rd16', 'Cloud solutions architect experienced in designing and implementing cloud-based solutions for businesses.', 2,1500),
        (17, 'Aiden Adams', 'aidenadams', 'aidenadams@email.com', 'Data Engineer', 'P@ssw0rd17', 'Data engineer specializing in data pipeline development and data warehousing. Proficient in data integration and ETL processes.', 2, 2400),
        (18, 'Grace Hill', 'gracehill', 'gracehill@email.com', 'DevSecOps Engineer', 'P@ssw0rd18', 'DevSecOps engineer focused on integrating security practices into the DevOps pipeline. Skilled in security testing and compliance.', 2, 5000),
        (19, 'Lucas Ward', 'lucasward', 'lucasward@email.com', 'Machine Learning Engineer', 'P@ssw0rd19', 'Machine learning engineer with a passion for developing predictive models and AI applications.', 2, 6000),
        (20, 'Lily Baker', 'lilybaker', 'lilybaker@email.com', 'Technical Writer', 'P@ssw0rd20', 'Technical writer skilled in creating documentation for software products and user guides.', 2, 7500);

    -- Insert 10 authors for the third project (project_id = 3)
    INSERT INTO authors (author_id, full_name, username, email, role, password, bio, project_id, salary)
    VALUES
        (21, 'Liam Adams', 'liamadams', 'liamadams@email.com', 'Software Developer', 'P@ssw0rd21', 'Experienced software developer with a passion for creating efficient and elegant code. Proficient in various programming languages and frameworks.', 3, 1700),
        (22, 'Aria Hall', 'ariahall', 'ariahall@email.com', 'Quality Assurance Engineer', 'P@ssw0rd22', 'Detail-oriented QA engineer with a focus on ensuring software quality and reliability. Experienced in manual and automated testing.', 3, 4500),
        (23, 'Ethan King', 'ethanking', 'ethanking@email.com', 'Frontend Developer', 'P@ssw0rd23', 'Frontend developer with a knack for crafting stunning user interfaces. Skilled in HTML, CSS, and JavaScript.', 3, 5600),
        (24,'Mila Baker', 'milabaker', 'milabaker@email.com', 'Backend Developer', 'P@ssw0rd24', 'Backend developer specializing in building scalable and performant server-side applications. Proficient in database design and optimization.', 3, 3400),
        (25, 'Noah Scott', 'noahscott', 'noahscott@email.com', 'UI/UX Designer', 'P@ssw0rd25', 'UI/UX designer focused on creating intuitive and visually appealing user experiences. Proficient in design tools and user research.', 3, 4500),
        (26,'Evelyn Turner', 'evelynturner', 'evelynturner@email.com', 'Scrum Master', 'P@ssw0rd26', 'Certified Scrum Master with a track record of facilitating agile development processes. Skilled in team collaboration and Agile methodologies.', 3, 3500),
        (27, 'Elijah Davis', 'elijahdavis', 'elijahdavis@email.com', 'DevOps Engineer', 'P@ssw0rd27', 'DevOps engineer with expertise in automation, continuous integration, and deployment. Dedicated to optimizing software delivery processes.', 3, 2500),
        (28, 'Aurora Lewis', 'auroralewis', 'auroralewis@email.com', 'Database Administrator', 'P@ssw0rd28', 'Database administrator responsible for managing and optimizing databases to ensure data integrity and performance.', 3, 5000),
        (29,'Grayson Wilson', 'graysonwilson', 'graysonwilson@email.com', 'Full Stack Developer', 'P@ssw0rd29', 'Full stack developer proficient in both frontend and backend technologies. Enjoys creating end-to-end solutions.', 3, 8400),
        (30, 'Luna Moore', 'lunamoore', 'lunamoore@email.com', 'System Architect', 'P@ssw0rd30', 'System architect focused on designing scalable and robust software architectures. Experienced in system integration and performance optimization.', 3, 1200);

    -- Insert a resource for the 'E-commerce Website Redesign' project
    INSERT INTO resources (resource_id, name, archive, description, project_id)
    VALUES
        (1, 'Design Mockups for E-commerce Redesign', 0, 'Design mockups for the user interface of the E-commerce Website Redesign project.', 1);

    -- Insert a resource for the 'Mobile App Development: Task Manager' project
    INSERT INTO resources (resource_id, name, archive, description, project_id)
    VALUES
        (2, 'Wireframes for Task Manager Mobile App', 0, 'Wireframes and user interface design for the Task Manager mobile app.', 2);

    -- Insert a resource for the 'Financial Analytics Dashboard' project
    INSERT INTO resources (resource_id, name, archive, description, project_id)
    VALUES
        (3, 'Data Sources for Financial Analytics', 0, 'Data sources and datasets used for the Financial Analytics Dashboard project.', 3);


    INSERT INTO notes (note_id, title, tags, archive, creation_date, content, resource_id)
    VALUES
        (1, 'UI/UX Feedback Meeting', 'UI/UX, Design', 0, GETDATE(), 'In our UI/UX feedback meeting, we discussed the initial mockups and gathered feedback for improvements.', 1),
        (2, 'User Testing Results', 'User Testing, Feedback', 0, GETDATE(), 'Results from the latest round of user testing sessions. Noted areas of concern and suggestions for enhancements.', 1),
        (3, 'Color Palette Selection', 'Design, Color Palette', 0, GETDATE(), 'Exploring color palettes for the redesign. Leaning towards a modern and vibrant palette.', 1),
        (4,'Competitor Analysis', 'Competitor Analysis', 0, GETDATE(), 'Summary of our latest competitor analysis findings. Identifying areas where we can outperform the competition.', 1),
        (5, 'Responsive Design Considerations', 'Responsive Design, Mobile', 0, GETDATE(), 'Discussion on making the website fully responsive to provide an optimal user experience on all devices.', 1),
        (6, 'Call to Action Buttons', 'UI/UX, Call to Action', 0, GETDATE(), 'Deciding on the style and placement of call-to-action buttons to drive conversions.', 1),
        (7, 'Homepage Redesign Ideas', 'Design, Homepage', 0, GETDATE(), 'Brainstorming ideas for a fresh homepage design that showcases our products effectively.', 1),
        (8, 'Typography Choices', 'Typography, Design', 0, GETDATE(), 'Choosing the right fonts and typography styles to enhance the overall design.', 1),
        (9, 'Navigation Menu Redesign', 'UI/UX, Navigation', 0, GETDATE(), 'Exploring options for a more intuitive and user-friendly navigation menu.', 1),
        (10, 'Feedback from Stakeholder Meeting', 'Feedback, Stakeholder', 0, GETDATE(), 'Key takeaways from the recent stakeholder meeting, including their feedback and expectations.', 1);


    INSERT INTO notes (note_id, title, tags, archive, creation_date, content, resource_id)
    VALUES
        (11, 'User Flow Diagram', 'User Flow, Wireframes', 0, GETDATE(), 'User flow diagram outlining the steps users will take in the Task Manager mobile app.', 2),
        (12, 'Wireframe Iteration 1', 'Wireframes, UI Design', 0, GETDATE(), 'Initial wireframe designs for the app screens. Feedback needed for improvements.', 2),
        (13, 'Task Creation Process', 'UI/UX, Task Management', 0, GETDATE(), 'Description of the task creation process and associated user interface elements.', 2),
        (14, 'UI Component Library', 'UI Components, Design', 0, GETDATE(), 'Exploring the creation of a UI component library for consistent design and development.', 2),
        (15, 'Accessibility Features', 'Accessibility, Mobile', 0, GETDATE(), 'Discussion on making the app accessible to users with disabilities.', 2),
        (16,'Feedback from Alpha Testing', 'Alpha Testing, Feedback', 0, GETDATE(), 'Received feedback from the alpha testing phase and identified areas for enhancement.', 2),
        (17, 'Progress Tracking Dashboard', 'UI/UX, Dashboard', 0, GETDATE(), 'Planning for the development of a progress tracking dashboard within the app.', 2),
        (18, 'User Profile Management', 'User Profile, Mobile App', 0, GETDATE(), 'Ideas for user profile management features and screens.', 2),
        (19,'Task Manager App Features', 'Feature Set, Mobile App', 0, GETDATE(), 'List of features to be included in the Task Manager mobile app.', 2),
        (20, 'Feedback from Beta Testing', 'Beta Testing, Feedback', 0, GETDATE(), 'Summary of feedback gathered during beta testing and proposed updates.', 2);


    INSERT INTO notes (note_id, title, tags, archive, creation_date, content, resource_id)
    VALUES
        (21, 'Financial Data Providers', 'Data Sources, Financial Data', 0, GETDATE(), 'List of financial data providers and sources used for the analytics dashboard.', 3),
        (22, 'Data Integration Process', 'Data Integration, Analytics', 0, GETDATE(), 'Explanation of the data integration process for aggregating financial data.', 3),
        (23, 'Data Cleansing and Validation', 'Data Cleansing, Quality', 0, GETDATE(), 'Details about data cleansing and validation procedures to ensure data quality.', 3),
        (24, 'Financial Metrics Definitions', 'Financial Metrics, Analytics', 0, GETDATE(), 'Definitions of key financial metrics tracked by the analytics dashboard.', 3),
        (25, 'Data Transformation Techniques', 'Data Transformation, Analytics', 0, GETDATE(), 'Methods used for transforming raw data into actionable insights.', 3),
        (26, 'Data Visualization Approaches', 'Data Visualization, Dashboard', 0, GETDATE(), 'Exploring data visualization techniques to present financial insights effectively.', 3),
        (27, 'Stakeholder Meeting Summary', 'Stakeholder Meeting, Feedback', 0, GETDATE(), 'Summary of the latest stakeholder meeting and their feedback on the analytics dashboard.', 3),
        (28, 'Performance Optimization', 'Performance, Analytics', 0, GETDATE(), 'Discussion on optimizing the performance of the analytics dashboard for faster data retrieval.', 3),
        (29,'Dashboard User Interface', 'UI/UX, Dashboard', 0, GETDATE(), 'Planning for the user interface design of the financial analytics dashboard.', 3),
        (30, 'Analytics Roadmap', 'Roadmap, Analytics', 0, GETDATE(), 'Outline of the future development and expansion of the analytics dashboard.', 3);

    INSERT INTO tasks (task_id, name, due, project_id, status, author_id)
    VALUES
        (1, 'User Interface Redesign', '2023-11-10', 1, 0, 5),
        (2, 'Mobile Optimization', '2023-11-15', 1, 0, 2),
        (3, 'Performance Testing', '2023-11-20', 1, 0, 10),
        (4, 'Checkout Process Enhancement', '2023-11-25', 1, 0, 6),
        (5, 'SEO and Marketing Strategy', '2023-11-30', 1, 0, 7);

    INSERT INTO tasks (task_id, name, due, project_id, status, author_id)
    VALUES
        (6, 'Wireframe Review Meeting', '2023-11-12', 2, 0, 12),
        (7, 'Backend Development', '2023-11-17', 2, 0, 14),
        (8, 'User Testing Phase 2', '2023-11-22', 2, 0, 16),
        (9, 'Integration Testing', '2023-11-27', 2, 0, 16),
        (10, 'App Launch Preparation', '2023-12-03', 2, 0, 19);


    INSERT INTO tasks (task_id, name, due, project_id, status, author_id)
    VALUES
        (11, 'Data Source Integration', '2023-11-15', 3, 0, 21),
        (12, 'Dashboard UI Design', '2023-11-20', 3, 0, 21),
        (13, 'Data Validation and Cleaning', '2023-11-25', 3, 0, 25),
        (14, 'User Acceptance Testing', '2023-11-30', 3, 0, 23),
        (15, 'Analytics Dashboard Deployment', '2023-12-05', 3, 0, 24);

    -- Insert data into the 'authors_notes' table
    INSERT INTO authors_notes (note_id, author_id)
    VALUES
        (1, 3),  -- Note ID 1 is associated with Author ID 3
        (2, 4),  -- Note ID 2 is associated with Author ID 4
        (3, 5),  -- Note ID 3 is associated with Author ID 5
        (4, 6),  -- Note ID 4 is associated with Author ID 6
        (5, 9),  -- Note ID 5 is associated with Author ID 9
        (6, 10), -- Note ID 6 is associated with Author ID 10
        (7, 3),  -- Note ID 7 is associated with Author ID 3
        (8, 4),  -- Note ID 8 is associated with Author ID 4
        (9, 5),  -- Note ID 9 is associated with Author ID 5
        (10, 7), -- Note ID 10 is associated with Author ID 7
        (11, 12), -- Note ID 11 is associated with Author ID 12
        (12, 12), -- Note ID 12 is associated with Author ID 12
        (13, 13), -- Note ID 13 is associated with Author ID 13
        (14, 14), -- Note ID 14 is associated with Author ID 14
        (15, 15), -- Note ID 15 is associated with Author ID 15
        (16, 12), -- Note ID 16 is associated with Author ID 12
        (17, 13), -- Note ID 17 is associated with Author ID 13
        (18, 16), -- Note ID 18 is associated with Author ID 16
        (19, 16), -- Note ID 19 is associated with Author ID 16
        (20, 17), -- Note ID 20 is associated with Author ID 17
        (21, 21), -- Note ID 21 is associated with Author ID 21
        (22, 21), -- Note ID 22 is associated with Author ID 21
        (23, 22), -- Note ID 23 is associated with Author ID 22
        (24, 23), -- Note ID 24 is associated with Author ID 23
        (25, 24), -- Note ID 25 is associated with Author ID 24
        (26, 21), -- Note ID 26 is associated with Author ID 21
        (27, 24), -- Note ID 27 is associated with Author ID 24
        (28, 22), -- Note ID 28 is associated with Author ID 22
        (29, 23), -- Note ID 29 is associated with Author ID 23
        (30, 22); -- Note ID 30 is associated with Author ID 22


    update tasks
    set status = 1
    where (task_id < 5 or task_id >= 25)  and status = 0;


    update authors
    set role = 'Project Leader'
    where username like '%alicesmith%' or role = 'Scrum Master';

    update notes
    set archive = 1
    where tags like '%UI/UX%' or (tags in ('Beta Testing, Feedback', 'User Testing, Feedback'));


    delete
    from authors_notes
    where (author_id between 28 and 30);

    delete
    from authors
    where (author_id <= 30 and author_id >= 28);

    delete
    from tasks
    where status = 1 or status is null;


    -- Insert Audio Entities
    INSERT INTO audios (audio_id, title, type, description, size, creator, duration, format)
    VALUES
        (1, 'UI/UX Feedback Meeting Audio', 'Meeting Audio', 'Audio recording of the UI/UX feedback meeting discussion.', 10240, 'John Doe', '00:15:30', 'MP3'),
        (2, 'User Testing Results Audio', 'Test Results Audio', 'Audio recording of the user testing results presentation.', 8192, 'Jane Smith', '00:10:45', 'WAV'),
        (3, 'Color Palette Selection Audio', 'Design Audio', 'Discussion on color palette selection for the redesign.', 5120, 'John Doe', '00:08:20', 'MP3'),
        (4, 'Competitor Analysis Audio', 'Analysis Audio', 'Summary of competitor analysis findings.', 7168, 'John Doe', '00:12:15', 'WAV'),
        (5, 'Responsive Design Considerations Audio', 'Design Audio', 'Audio discussion on making the website fully responsive.', 6144, 'John Doe', '00:10:00', 'MP3');

    -- Insert Video Entities
    INSERT INTO videos (video_id, title, type, description, size, creator, duration, format)
    VALUES
        (1, 'UI/UX Feedback Meeting Video', 'Meeting Video', 'Video recording of the UI/UX feedback meeting discussion.', 25600, 'John Doe', '00:30:45', 'MP4'),
        (2, 'User Testing Results Video', 'Test Results Video', 'Video presentation of the user testing results.', 20480, 'Jane Smith', '00:25:20', 'AVI'),
        (3, 'Color Palette Selection Video', 'Design Video', 'Video discussion on color palette selection for the redesign.', 17408, 'John Doe', '00:28:10', 'MP4'),
        (4, 'Competitor Analysis Video', 'Analysis Video', 'Video summary of competitor analysis findings.', 22528, 'John Doe', '00:32:30', 'AVI'),
        (5, 'Responsive Design Considerations Video', 'Design Video', 'Video discussion on making the website fully responsive.', 19456, 'John Doe', '00:30:00', 'MP4');

    -- Insert Image Entities
    INSERT INTO images (image_id, title, type, creator, height, width, format)
    VALUES
        (1, 'UI/UX Feedback Meeting Image', 'Meeting Image', 'John Doe', 1080, 1920, 'JPEG'),
        (2, 'User Testing Results Image', 'Test Results Image', 'Jane Smith', 1200, 1920, 'PNG'),
        (3, 'Color Palette Selection Image', 'Design Image', 'John Doe', 900, 1600, 'JPEG'),
        (4, 'Competitor Analysis Image', 'Analysis Image', 'John Doe', 800, 1600, 'PNG'),
        (5, 'Responsive Design Considerations Image', 'Design Image', 'John Doe', 1080, 1920, 'JPEG');

    -- Insert Webclip Entities
    INSERT INTO webclips (webclip_id, title, link)
    VALUES
        (1, 'UI/UX Feedback Meeting Webclip', 'https://example.com/uiux-feedback-clip1'),
        (2, 'User Testing Results Webclip', 'https://example.com/usertesting-results-clip1'),
        (3, 'Color Palette Selection Webclip', 'https://example.com/colorpalette-clip1'),
        (4, 'Competitor Analysis Webclip', 'https://example.com/competitor-analysis-clip1'),
        (5, 'Responsive Design Considerations Webclip', 'https://example.com/responsive-design-clip1');


    insert into audios_notes (note_id, audio_id)
    values
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5);

    insert into videos_notes (note_id, video_id)
    values
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5);

    insert into images_notes (note_id, image_id)
    values
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5);

    insert into webclips_notes (note_id, webclip_id)
    values
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5);