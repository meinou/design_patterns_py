class Event:
    def __init__(self, name, required_experience):
        self.name = name
        self.required_experience = required_experience

    def print(self):
        print(self.name + " requires " + self.required_experience);


class InterdisciplinaryEvent:
    def __init__(self, base_event):
        self.name = "Interdisciplinary " + base_event.name
        self.required_experience = base_event.required_experience + 2


class InternationalEvent:
    def __init__(self, base_event):
        self.name = "International " + base_event.name
        self.required_experience = base_event.required_experience + 4


class Speaker:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
        self.events = []

    def speak(self, event):
        if event.required_experience > self.experience:
            print(self.name + " does not have enough experience to speak at " + event.name)
        else:
            print(self.name + " is speaking at the " + event.name)
            self.experience += event.required_experience
            self.events.append(event)

    def print_status(self):
        print(self.name + " spoke at" + str(len(self.events)) + " events: ")
        for event in self.events:
            print("  * " + event.name)
        print("this speaker has " + str(self.experience) + " level of experience");


dina = Speaker('Dina', 1)
meetup = Event('Meetup', 2)
party = Event('Party', 1)
conference = Event("Conference", 5)

interdisciplinary_meetup = InterdisciplinaryEvent(meetup)
international_interdisciplinary_meetup = InternationalEvent(interdisciplinary_meetup)
international_conference = InternationalEvent(conference)

dina.speak(party)
dina.speak(meetup)
dina.speak(conference)
dina.speak(interdisciplinary_meetup)

dina.print_status()
