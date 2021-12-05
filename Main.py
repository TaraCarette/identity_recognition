import Database
import FaceDetection


if __name__ == '__main__':
    # Connect to database and initialize
    database_conn = Database.connect_to_database()
    Database.initialize_database(database_conn)

    # Initialize face detection class and load model
    face_det = FaceDetection.FaceDetection()
    face_det.load_model(file='test')            #TODO add real model here later

    # Initialize robot
    robot = None
    # TODO Add robot class with functions and initialize

    # Start Main Loop #TODO account for situations where this loop is broken in the middle because someone walks away for example
    while True:

        # Get image from robot camera
        camera_image = None     #TODO Add function here to get camera image from robot

        # Perform face detection
        face_detected = face_det.get_closest_face(camera_image)

        # Query face from database
        user_id = Database.get_similar_face(face_detected)

        # Check if face is present in database and act appropriately
        if user_id:     # The case a face is present (a user_id is returned)
            # Retrieve preference
            preference = Database.get_user_preference(database_conn, user_id)
        else:       # The case a face is not (yet) present (no user_id is returned)
            preference = 0  #TODO For now just use default preference for new faces, change this later
            user_id = Database.add_new_face(database_conn, face_detected, preference)

        # Perform response
        #TODO Make robot perform preferred response

        # Receive feedback from robot sensor
        #TODO Receive feedback from robot sensor
        feedback = 0 # For now 0 means correct, -1 means a little less and 1 means a little more (this is just an idea of how we could implement this)

        # Adjust response until feedback is positive
        while not feedback == 0:
            # Adjust response
            #TODO adjust response of robot based on feedback

            # Perform response
            # TODO Make robot perform preferred response

            # Receive feedback from robot sensor
            # TODO Receive feedback from robot sensor
            feedback = 0  # For now 0 means correct, -1 means a little less and 1 means a little more (this is just an idea of how we could implement this)

        # Store correct response (preference) in database
        Database.set_user_preference(database_conn, user_id, preference)

        # For now restart loop but we could perform a wave motion here or some other interaction to signal goodbye
