//#include "Tests.h"
//#include <assert.h>
//#include <vector>
//
///// <summary>
///// EVENT TESTS
///// </summary>
//void testEvent() {
//	Date date;
//	Time time;
//	date.day = 5;
//	date.month = 10;
//	date.year = 2023;
//	time.hour = 8;
//	time.minute = 25;
//
//	Date date2;
//	Time time2;
//	date2.day = 3;
//	date2.month = 5;
//	date2.year = 2024;
//	time2.hour = 5;
//	time2.minute = 25;
//
//	Event event("Concert", "Cool!", date, time, 0, "www.facebook.com");
//
//	// 
//	assert(event.getDate().day == date.day);
//	assert(event.getDate().month == date.month);
//	assert(event.getDate().year == date.year);
//	assert(event.getTime().hour == time.hour);
//	assert(event.getTime().minute == time.minute);
//	assert(event.getDescription() == "Cool!");
//	assert(event.getLink() == "www.facebook.com");
//	assert(event.getNumberOfPeople() == 0);
//	assert(event.getTitle() == "Concert");
//
//	// COPY
//	Event copyEvent = event;
//	assert(copyEvent.getDate().day == event.getDate().day);
//	assert(copyEvent.getDate().day == event.getDate().day);
//	assert(copyEvent.getDate().day == event.getDate().day);
//	assert(copyEvent.getTime().hour == event.getTime().hour);
//	assert(copyEvent.getTime().minute == event.getTime().minute);
//	assert(event == copyEvent);
//
//	// SETTERS
//	event.setTitle("PoolParty");
//	assert(event.getTitle() == "PoolParty");
//	event.setDescription("Cool party!");
//	assert(event.getDescription() == "Cool party!");
//	event.setLink("www.youtube.com");
//	assert(event.getLink() == "www.youtube.com");
//	event.setNumberOfPeople(3);
//	assert(event.getNumberOfPeople() == 3);
//	event.setDate(date2);
//	event.setTime(time2);
//	assert(event.getDate().day == date2.day);
//	assert(event.getDate().month == date2.month);
//	assert(event.getDate().year == date2.year);
//	assert(event.getTime().hour == time2.hour);
//	assert(event.getTime().minute == time2.minute);
//
//}
//
///// <summary>
///// REPOSITORY TESTS
///// </summary>
//void testRepositoryAdd()
//{
//	// CREATE 3 EVENTS
//	Date date1, date2, date3;
//	Time time1, time2, time3;
//	date1.day = 1;
//	date2.day = 2;
//	date3.day = 3;
//	date1.month = 1;
//	date2.month = 2;
//	date3.month = 3;
//	date1.year = 2021;
//	date2.year = 2022;
//	date3.year = 2023;
//	time1.hour = 1;
//	time2.hour = 2;
//	time3.hour = 3;
//	time1.minute = 1;
//	time2.minute = 2;
//	time3.minute = 3;
//	Event event1("Event1", "Description1", date1, time1, 1, "link1");
//	Event event2("Event2", "Description2", date2, time2, 2, "link2");
//	Event event3("Event3", "Description3", date3, time3, 3, "link3");
//
//	// CREATE REPO
//	std::vector<Event> events;
//	Repository repository{"Events.txt", events};
//
//	// TEST ADD
//	repository.addEvent(event1);
//	assert(repository.getAllEvents().size() == 1);
//	repository.addEvent(event2);
//	assert(repository.getAllEvents().size() == 2);
//	repository.addEvent(event3);
//	assert(repository.getAllEvents().size() == 3);
//
//	// TEST NO ADD DUPLICATES
//	assert(repository.addEvent(event1) == false);
//	assert(repository.addEvent(event2) == false);
//	assert(repository.addEvent(event3) == false);
//
//	// TEST FIND
//	assert(repository.findEventPosition(event1) == 0);
//	assert(repository.findEventPosition(event2) == 1);
//	assert(repository.findEventPosition(event3) == 2);
//}
//
//void testRepositoryRemove()
//{
//	// CREATE 3 EVENTS
//	Date date1, date2, date3;
//	Time time1, time2, time3;
//	date1.day = 1;
//	date2.day = 2;
//	date3.day = 3;
//	date1.month = 1;
//	date2.month = 2;
//	date3.month = 3;
//	date1.year = 2021;
//	date2.year = 2022;
//	date3.year = 2023;
//	time1.hour = 1;
//	time2.hour = 2;
//	time3.hour = 3;
//	time1.minute = 1;
//	time2.minute = 2;
//	time3.minute = 3;
//	Event event1("Event1", "Description1", date1, time1, 1, "link1");
//	Event event2("Event2", "Description2", date2, time2, 2, "link2");
//	Event event3("Event3", "Description3", date3, time3, 3, "link3");
//
//	// CREATE REPO
//	std::vector<Event> events;
//	Repository repository{"Events.txt", events};
//
//	// TEST REMOVE NOT EXISTING
//	assert(repository.removeEvent(0) == false);
//
//	// ADD EVENTS
//	repository.addEvent(event1);
//	repository.addEvent(event2);
//	repository.addEvent(event3);
//
//
//	// TEST REMOVE
//	repository.removeEvent(0);
//	assert(repository.getAllEvents().size() == 2);
//	assert(repository.findEventPosition(event1) == -1);
//}
//
//void testRepositoryUpdate()
//{
//	// CREATE 3 EVENTS
//	Date date1, date2, date3;
//	Time time1, time2, time3;
//	date1.day = 1;
//	date2.day = 2;
//	date3.day = 3;
//	date1.month = 1;
//	date2.month = 2;
//	date3.month = 3;
//	date1.year = 2021;
//	date2.year = 2022;
//	date3.year = 2023;
//	time1.hour = 1;
//	time2.hour = 2;
//	time3.hour = 3;
//	time1.minute = 1;
//	time2.minute = 2;
//	time3.minute = 3;
//	Event event1("Event1", "Description1", date1, time1, 1, "link1");
//	Event event2("Event2", "Description2", date2, time2, 2, "link2");
//	Event event3("Event3", "Description3", date3, time3, 3, "link3");
//
//	// CREATE REPO
//	std::vector<Event> events;
//	Repository repository{"Events.txt", events };
//
//	// ADD EVENTS
//	repository.addEvent(event1);
//	repository.addEvent(event2);
//	repository.addEvent(event3);
//
//	// TEST UPDATE NOT GOOD POS
//	assert(repository.updateEvent(-1, event2) == false);
//
//	// TEST UPDATE
//	repository.updateEvent(0, event2);
//	assert(repository.getAllEvents()[0] == event2);
//	assert(repository.findEventPosition(event1) == -1);
//}
//
///// <summary>
///// USER SERVICE TESTS
///// </summary>
//void testUserServiceAdd()
//{
//	std::vector<Event> events;
//	Repository repository{"Events.txt", events};
//	UserService userService{ repository };
//
//	Date date1;
//	Time time1;
//	date1.day = 1;
//	date1.month = 1;
//	date1.year = 2021;
//	time1.hour = 1;
//	time1.minute = 1;
//	Event event1("Event1", "Description1", date1, time1, 1, "link1");
//	// ADD
//	userService.addEventToList(event1);
//	assert(userService.getEventList()[0] == event1);
//	assert(userService.getEventList().size() == 1);
//
//	// ADD ALREADY EXISTING
//	assert(userService.addEventToList(event1) == false);
//
//}
//
//void testUserServiceRemove()
//{
//	std::vector<Event> events;
//	Repository repository{"Events.txt", events };
//	UserService userService{ repository };
//
//	Date date1;
//	Time time1;
//	date1.day = 1;
//	date1.month = 1;
//	date1.year = 2021;
//	time1.hour = 1;
//	time1.minute = 1;
//	Event event1("Event1", "Description1", date1, time1, 1, "link1");
//
//	// REMOVE NOT EXISTING
//	assert(userService.removeEventFromList(event1.getTitle(), event1.getDescription()) == false);
//
//	userService.addEventToList(event1);
//
//	// REMOVE THE ELEMENT
//	userService.removeEventFromList(event1.getTitle(), event1.getDescription());
//	assert(userService.getEventList().size() == 0); // test if the userService events is now empty
//
//}
//
//void testUserServiceGetByMonth()
//{
//	std::vector<Event> events;
//	Repository repository{"Events.txt", events };
//	UserService userService{ repository };
//
//	Date date1;
//	Time time1;
//	date1.day = 1;
//	date1.month = 1;
//	date1.year = 2021;
//	time1.hour = 1;
//	time1.minute = 1;
//	Event event1("Event1", "Description1", date1, time1, 1, "link1");
//	userService.addEventToList(event1);
//
//	// SEARCH BY MONTH
//	assert(userService.getEventOfGivenMonth(userService.getEventList(), 1)[0] == event1);
//}
//
///// <summary>
///// ADMINISTRATOR SERVICE TESTS
///// </summary>
//void testAdministratorServiceAdd()
//{
//	std::vector<Event> events;
//	Repository repository{"Events.txt" events };
//	AdministratorService administratorService{ repository };
//
//	Date date1;
//	Time time1;
//	date1.day = 1;
//	date1.month = 1;
//	date1.year = 2021;
//	time1.hour = 1;
//	time1.minute = 1;
//	Event event1("Event1", "Description1", date1, time1, 1, "link1");
//	Event event2("Event1", "Description1", date1, time1, 2, "link1");
//
//	// ADD
//	administratorService.addEvent(event1.getTitle(), event1.getDescription(), event1.getDate(), event1.getTime(), event1.getNumberOfPeople(), event1.getLink());
//	assert(administratorService.getAllEvents().size() == 1);
//	assert(administratorService.getAllEvents()[0] == event1);
//
//	// INCREASE NUMBER OF PEOPLE
//	administratorService.increaseNumberOfPeople(event1.getTitle(), event1.getDescription());
//	assert(administratorService.getAllEvents()[0] == event2);
//}
//
//void testAdministratorServiceRemove()
//{
//	std::vector<Event> events;
//	Repository repository{"Events.txt", events };
//	AdministratorService administratorService{ repository };
//
//	Date date1;
//	Time time1;
//	date1.day = 1;
//	date1.month = 1;
//	date1.year = 2021;
//	time1.hour = 1;
//	time1.minute = 1;
//	Event event1("Event1", "Description1", date1, time1, 1, "link1");
//	Event event2("Event2", "Description2", date1, time1, 2, "link2");
//
//	//add the 2 events
//	administratorService.addEvent(event1.getTitle(), event1.getDescription(), event1.getDate(), event1.getTime(), event1.getNumberOfPeople(), event1.getLink());
//	administratorService.addEvent(event2.getTitle(), event2.getDescription(), event2.getDate(), event2.getTime(), event2.getNumberOfPeople(), event2.getLink());
//	assert(administratorService.getAllEvents().size() == 2);
//	//REMOVE EVENT1
//	administratorService.removeEvent(event2.getTitle(), event2.getDescription());
//	assert(administratorService.getAllEvents().size() == 1);
//	assert(administratorService.getAllEvents()[0] == event1);
//
//}
//
//void testAdministratorServiceUpdate()
//{
//	std::vector<Event> events;
//	Repository repository{"Events.txt", events };
//	AdministratorService administratorService{ repository };
//
//	Date date1;
//	Time time1;
//	date1.day = 1;
//	date1.month = 1;
//	date1.year = 2021;
//	time1.hour = 1;
//	time1.minute = 1;
//	Event event1("Event1", "Description1", date1, time1, 1, "link1");
//
//	//add the 2 events
//	administratorService.addEvent(event1.getTitle(), event1.getDescription(), event1.getDate(), event1.getTime(), event1.getNumberOfPeople(), event1.getLink());
//
//	//update the event
//	administratorService.updateEvent(event1.getTitle(), event1.getDescription(), "1", "1", date1, time1, 100, "no");
//	Event updatedEvent("1", "1", date1, time1, 100, "no");
//	assert(administratorService.getAllEvents().size() == 1);
//	assert(administratorService.getAllEvents()[0] == updatedEvent);
//}
//
//void testAdministratorServiceGenerators()
//{
//	std::vector<Event> events;
//	Repository repository{"Events.txt", events };
//	AdministratorService administratorService{ repository };
//	administratorService.generateEvents();
//
//	// TEST GENERATE EVENTS 
//	assert(administratorService.getAllEvents().size() == 10);
//	// TEST DATE GENERATOR
//	Date date = administratorService.generateDate();
//	assert(date.day >= 1 && date.day <= 31);
//	assert(date.month >= 1 && date.month <= 12);
//	assert(date.year >= 2000 && date.year <= 2100);
//	// TEST TIME GENERATOR
//	Time time = administratorService.generateTime();
//	assert(time.hour < 24 && time.hour >= 0);
//	assert(time.minute < 60 && time.minute >= 0);
//}
//
//
//
///// <summary>
///// RUN ALL TESTS
///// </summary>
//void runAllTests()
//{
//	//event
//	testEvent();
//	//repository
//	testRepositoryAdd();
//	testRepositoryRemove();
//	testRepositoryUpdate();
//	//user service
//	testUserServiceAdd();
//	testUserServiceRemove();
//	testUserServiceGetByMonth();
//	//admin service
//	testAdministratorServiceAdd();
//	testAdministratorServiceRemove();
//	testAdministratorServiceUpdate();
//	testAdministratorServiceGenerators();
//}
