import orbit
import astro_pi_replay
import picamera
import exif
iss = orbit.ISS
replay = astro_pi_replay.replay
PiCamera = picamera.PiCamera


cam = PiCamera()
cam.resolution = (4056,3040)

def convert(angle):
    sign, degrees, minutes, seconds = angle.signed_dms()
    exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, exif_angle

def custom_capture(iss, camera, image):
    point = iss.coordinates()
    south, exif_latitude = convert(point.latitude)
    west, exif_longitude = convert(point.longitude)

    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # Instead of capturing an image using the PiCamera object,
    # use the replay.capture() function to capture a picture using the Astro Pi Replay tool
    replay.capture()

# Call the custom_capture function with the necessary parameters
custom_capture(iss(), cam, "gps_image1.jpg")