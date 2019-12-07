import greeter

def test_case1() :
	assert greeter.greetingsGenerator(["Athos",  "Porthos",  "Aramis"]) == ["Hello, Athos!",  "Hello, Porthos!",  "Hello, Aramis!"]

def test_case2() :
        assert greeter.greetingsGenerator(["Fifer",  "Fiddler",  "Edmund"]) == ["Hello, Fifer!",  "Hello, Fiddler!",  "Hello, Edmund!"]

def test_case3() :
        assert greeter.greetingsGenerator([]) == []

def test_case4() :
        assert greeter.greetingsGenerator(["Dwarf",  "Doc",  "Dopey",  "Bashful",  "Grumpy",  "Sneezy",  "Sleepy",  "Happy"]) == ["Hello, Dwarf!",  "Hello, Doc!",  "Hello, Dopey!",  "Hello, Bashful!",  "Hello, Grumpy!",  "Hello, Sneezy!",  "Hello, Sleepy!",  "Hello, Happy!"]

def test_case5() :
        assert greeter.greetingsGenerator(["Hero"]) == ["Hello, Hero!"]
