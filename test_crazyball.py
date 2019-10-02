import crazyball

def test_case1() :
	assert crazyball.crazyball(["Ninja",  "Warrior",  "Trainee",  "Newbie"] ,3 ) == [["Newbie","Ninja","Trainee"], ["Newbie","Ninja","Warrior"], ["Newbie","Trainee","Warrior"],["Ninja","Trainee","Warrior"]]

def test_case2() :
        assert crazyball.crazyball(["Ninja",  "Warrior",  "Trainee",  "Newbie"] ,4) == [["Newbie","Ninja","Trainee","Warrior"]]

def test_case3() :
        assert crazyball.crazyball(["Pooh"],1) == [["Pooh"]]

def test_case4() :
        assert crazyball.crazyball(["Browny",  "Whitey",  "Blacky"] ,1 ) == [["Blacky"],  ["Browny"],  ["Whitey"]]

