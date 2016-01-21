

class Game(object):
    """

        beta stage

        Usage;

            game = Game(request, story, chapter)
            game.resume()

        Storage;

            current_chapter_(current_story_id) = x
            current_snippet_(current_chapter_id) = y

    """
    ch_key = None
    sn_key = None

    def __init__(self, request, story=None, chapter=None):
        self.chapter = chapter or story.first_chapter
        self.story = story or self.chapter.story
        self.request = request
        # set keys
        self.ch_key = "current_chapter_" + str(self.story.id)
        self.sn_key = "current_snippet_" + str(self.chapter.id)

    def start(self):
        self.move(
            chapter.get_starting_snippet()
        )

    def move(self, s_id):
        self.set_snippet(s_id)

    def resume(self):
        self.set_snippet(
            self.get_current_snippet_id()
        )

    def reset(self):
        self.set_snippet(self.chapter.first_snippet.id)

    def get_current_snippet_id(self):
        try:
            return self.request.session[self.sn_key]
        except:
            self.request.session[self.sn_key] = self.chapter.first_snippet.id
            return self.chapter.first_snippet.id

    def set_snippet(self, s_id):
        self.request.session[self.sn_key] = s_id

