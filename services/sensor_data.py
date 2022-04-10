class SensorData:
    def __init__(self, user_id=None, timestamp=None, heart_rate=None, respiration_rate=None, activity=None):
        self.__user_id = user_id
        self.__timestamp = timestamp
        self.__heart_rate = heart_rate
        self.__respiration_rate = respiration_rate
        self.__activity = activity

    def get_user_id(self):
        return self.__user_id

    def get_timestamp(self):
        return self.__timestamp

    def get_heart_rate(self):
        return self.__heart_rate

    def get_respiration_rate(self):
        return self.__respiration_rate

    def get_activity(self):
        return self.__activity

    def to_json(self):
        return {"user_id": self.__user_id, "timestamp": self.__timestamp, "heart_rate": self.__heart_rate,
                "respiration_rate": self.__respiration_rate, "activity": self.__activity}

    def to_obj(self, json_data):
        self.__user_id = json_data['user_id']
        self.__timestamp = json_data["timestamp"]
        self.__heart_rate = json_data["heart_rate"]
        self.__respiration_rate = json_data["respiration_rate"]
        self.__activity = json_data['activity']
        return self
