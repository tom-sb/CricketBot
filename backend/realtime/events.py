WEBSOCKET_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

class NewDataEvent:
    def __init__(self, id, topic, payload, timestamp, qos):
        self._type = "data-sensor"
        self._id = id
        self._topic = topic
        self._payload = payload
        self._timestamp = timestamp
        self._qos = qos
    
    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id
    
    @property
    def topic(self):
        return self._topic
    
    @property
    def payload(self):
        return self._payload
    
    @property
    def timestamp(self):
        return self._timestamp.strftime(WEBSOCKET_DATETIME_FORMAT)
    
    @property
    def qos(self):
        return self._qos
    
    @property
    def properties_dict(self):
        return dict(
            type=self.type,
            id=self.id,
            topic= self.topic,
            payload=self.payload,
            timestamp=self.timestamp,
            qos = self.qos,
        )

class NewDataImage:
    def __init__(self, id, image):
        self._type = "data-image"
        self._id = id
        self._image = image
    
    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id
    
    @property
    def image(self):
        return self._image.url
    
    @property
    def properties_dict(self):
        return dict(
            type=self.type,
            id=self.id,
            image=self.image,
        )