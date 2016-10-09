import readline


class Completer(object):

    @classmethod
    def install_new_completer(cls, options):
        completer = cls(options)
        readline.set_completer(completer.complete)
        readline.set_completer_delims('')  # allow options with whitespace
        readline.parse_and_bind('tab: complete')

    def __init__(self, options):
        self.options = options

    def complete(self, text, state):
        text = text.lower()
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options
                                    if s and s.lower().startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None
