#include "UnitTests.h"
#include "FakeRepository.h"

void UnitTests::testServiceAdd()
{
	FakeRepository* fakeRepo = new FakeRepository{};
	AdministratorService admin{fakeRepo};
	Date date1 = Date{ 2023,10,2 };
	Time time1 = Time{ 10,10 };
	assert(admin.addEvent("NACHO", "CEL MAI TARE", date1, time1, 3, "www.youtube.com") == true);
	fakeRepo->boolValue = false;
	assert(admin.addEvent("NACHO", "CEL MAI TARE", date1, time1, 3, "www.youtube.com") == false);
}

void UnitTests::testServiceRemove()
{
	FakeRepository* fakeRepo = new FakeRepository{};
	AdministratorService admin{ fakeRepo };
	assert(admin.removeEvent("Nach0", "Rapadungadunga, la pirat e")==true);
	fakeRepo->boolValue = false;
	assert(admin.removeEvent("Nach0", "Rapadungadunga, la pirat e") == false);
}

void UnitTests::testGetByTitle()
{
	FakeRepository* fakeRepo = new FakeRepository{};
	AdministratorService admin{ fakeRepo };
	Date date1 = Date{ 2023,10,2 };
	Time time1 = Time{ 10,10 };
	Event event1{ "NACHO", "CEL MAI TARE", date1, time1, 3, "www.youtube.com" };
	Event event2{ "NACHO2", "CEL MAI TARE!", date1, time1, 3, "www.youtube.com" };
	assert(admin.getEventByTitle("NACHO") == event1);
	Date date;
	Time time;
	date.day = 1;
	date.month = 1;
	date.year = 1;
	time.hour = 1;
	time.minute = 1;
	Event emptyEvent{ "","",date, time,1,"" };
	assert(admin.getEventByTitle("Cornelius") == emptyEvent);
}

void UnitTests::runAllTests()
{
	this->testServiceAdd();
	this->testServiceRemove();
}
