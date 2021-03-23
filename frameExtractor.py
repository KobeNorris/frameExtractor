import cv2


class FrameExtractor:
    frameInterval = 10
    imageMax = 1000

    def extractFromCamera(self):
        imgIndex = 1
        frameIndex = 1

        # cap = cv2.VideoCapture('C:/Users/kobew/Desktop/video/sample.mp4')
        cap = cv2.VideoCapture(0)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False | imgIndex == FrameExtractor.imageMax:
                break

            if frameIndex == 1:
                cv2.imwrite('frame/frame'+str(imgIndex * 10 - 9)+'.jpg', frame)
                imgIndex += 1
                frameIndex = FrameExtractor.frameInterval
            else:
                frameIndex -= 1

        cap.release()
        cv2.destroyAllWindows()

    def extractFromVideo(self, videoPath):
        imgIndex = 1
        frameIndex = 1

        # cap = cv2.VideoCapture('C:/Users/kobew/Desktop/video/sample.mp4')
        cap = cv2.VideoCapture(videoPath)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False | imgIndex == FrameExtractor.imageMax:
                break

            if frameIndex == 1:
                cv2.imwrite('frame/frame'+str(imgIndex * 10 - 9)+'.jpg', frame)
                imgIndex += 1
                frameIndex = FrameExtractor.frameInterval
            else:
                frameIndex -= 1

        cap.release()
        cv2.destroyAllWindows()

    def extractFromVideoAndRange(self, videoPath, start, end):
        imgIndex = 1
        frameIndex = 1

        # cap = cv2.VideoCapture('C:/Users/kobew/Desktop/video/sample.mp4')
        cap = cv2.VideoCapture(videoPath)
        while(cap.isOpened()):
            while cap.get(0) > start & cap.get(0) < end:
                ret, frame = cap.read()
                if ret == False | imgIndex == FrameExtractor.imageMax:
                    break

                if frameIndex == 1:
                    cv2.imwrite('frame/frame' +
                                str(imgIndex * 10 - 9)+'.jpg', frame)
                    imgIndex += 1
                    frameIndex = FrameExtractor.frameInterval
                else:
                    frameIndex -= 1

        cap.release()
        cv2.destroyAllWindows()


# Main
util = FrameExtractor()
util.extractFromCamera()
