#TODO Add model and other parameters and complete functions.
class FaceDetection:
    model = None

    def __init__(self):
        pass

    def detect_faces(self, camera_image):
        raise NotImplementedError

        return

    def get_closest_face(self, camera_image):
        # Detect all faces in image
        faces = self.detect_faces(camera_image)

        # Return closest face based on sonar information
        raise NotImplementedError

        return

    def train_model(self, X, y):
        raise NotImplementedError

    def load_model(self, file):
        raise NotImplementedError

    def save_model(self, file_name):
        raise NotImplementedError

if __name__ == '__main__':
    pass