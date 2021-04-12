class Problem:
    ID = set()
    next_available_ID = 0

    def __init__(self, 
                    Metadata =  { 
                                    "FileName"    : "",
                                    "Title"       : "",
                                    "Difficulty"  : "",
                                    "Category"    : "",
                                    "Tags"        : set(),
                                    "Source"      : set(),
                    }, 
                    Question =  "", 
                    Answer   =  ""
    ):
        Problem.next_available_ID += 1
        Problem.ID.add(Problem.next_available_ID)
        self.ID         = Problem.next_available_ID

        self.Metadata   = Metadata        
        self.Question   = Question
        self.Answer     = Answer