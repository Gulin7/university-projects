import entities
import operations
import ui


def run_all_tests():
    test_add_function()
    test_insert_function()
    test_remove_function()
    test_replace_function()


def test_add_function():
    contestants = []
    scores = [1, 3, 4]
    assert len(contestants) == 0
    operations.add_contestant(contestants, *scores)
    assert len(contestants) == 1
    assert contestants[0]["p1"] == scores[0]
    assert contestants[0]["p2"] == scores[1]
    assert contestants[0]["p3"] == scores[2]
    scores = [1, 15, -3]
    operations.add_contestant(contestants, *scores)
    assert len(contestants) == 2
    print("<add> test -> success!")


def test_insert_function():
    contestants = []
    scores = [1, 4, 8]
    position = 1
    operations.add_contestant(contestants, *scores)
    operations.add_contestant(contestants, *scores)
    operations.add_contestant(contestants, *scores)
    insert = ['1', '3', '7', 'at', '2']
    assert len(contestants) == 3
    ui.insert_contestant(contestants, *insert)
    assert len(contestants) == 4
    assert contestants[position - 1]["p1"] == scores[0]
    assert contestants[position - 1]["p2"] == scores[1]
    assert contestants[position - 1]["p3"] == scores[2]
    print("<insert> test -> success!")


def test_remove_function():
    contestants = []
    scores = [3, 2, 3]
    operations.add_contestant(contestants, *scores)
    operations.add_contestant(contestants, *scores)
    operations.add_contestant(contestants, *scores)
    assert len(contestants) == 3
    ui.remove_contestant(contestants, 1)
    assert contestants[0]["p1"] == 0
    assert contestants[0]["p2"] == 0
    assert contestants[0]["p3"] == 0
    ui.remove_contestant(contestants, 2, "to", 3)
    assert contestants[1]["p1"] == 0
    assert contestants[1]["p2"] == 0
    assert contestants[1]["p3"] == 0
    assert contestants[2]["p1"] == 0
    assert contestants[2]["p2"] == 0
    assert contestants[2]["p3"] == 0
    print("<remove> test -> success!")


def test_replace_function():
    contestants = []
    scores = [3, 2, 3]
    operations.add_contestant(contestants, *scores)
    operations.add_contestant(contestants, *scores)
    operations.add_contestant(contestants, *scores)
    assert contestants[0]["p1"] == 3
    assert contestants[0]["p2"] == 2
    assert contestants[0]["p3"] == 3
    ui.replace_contestant(contestants, 1, "P1", "with", 10)
    assert contestants[0]["p1"] == 10
    ui.replace_contestant(contestants, 1, "P2", "with", 2)
    assert contestants[0]["p1"] == 10
    assert contestants[0]["p2"] == 2
    assert contestants[0]["p3"] == 3
    ui.replace_contestant(contestants, 1, "P3", "with", 1)
    assert contestants[0]["p1"] == 10
    assert contestants[0]["p2"] == 2
    assert contestants[0]["p3"] == 1
    print("<replace> test -> success!")
