import OpenImageIO as oiio
import glob
import cv2

if __name__ == '__main__':

    for path in glob.glob('/foo/bar/*.exr'):
        print(path)
        jpg_path = path.replace('.exr', '_txt.jpg')

        #Read File
        buf = oiio.ImageBuf(path)

        #to Numpy Array
        nd = buf.get_pixels(oiio.FLOAT)

        #Shuffle
        nd = cv2.cvtColor(nd, cv2.COLOR_RGB2BGR)

        #Draw Text
        colorBGR = (0.0, 0.0, 1.0)

        cv2.putText(img=nd,
                    text="OpenCV",
                    org=(50, 100),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=2,
                    color=colorBGR,
                    thickness=15)

        #De-Shuffle
        nd = cv2.cvtColor(nd, cv2.COLOR_BGR2RGB)

        #Back to oiio
        buf.set_pixels(oiio.ROI(), nd)

        #Write File
        buf.write(jpg_path)
