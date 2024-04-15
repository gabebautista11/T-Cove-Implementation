class Query:
    def __init__(self):
        self.user_id = None
        self.start_time = None
        self.end_time = None
        self.semantic_mode = None 
        self.time_threshold = None
        self.confidence_threshold = None
        self.contact_mode = None 

    def get_contact_mode(self):
        return self.contact_mode

    def set_contact_mode(self, contact_mode):
        self.contact_mode = contact_mode

    def get_time_threshold(self):
        return self.time_threshold

    def set_time_threshold(self, time_threshold):
        self.time_threshold = time_threshold

    def get_confidence_threshold(self):
        return self.confidence_threshold

    def set_confidence_threshold(self, confidence_threshold):
        self.confidence_threshold = confidence_threshold

    def get_semantic_mode(self):
        return self.semantic_mode

    def set_semantic_mode(self, semantic_mode):
        self.semantic_mode = semantic_mode

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end_time):
        self.end_time = end_time
