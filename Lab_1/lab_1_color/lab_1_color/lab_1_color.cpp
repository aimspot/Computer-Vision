#include <iostream>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/core/core.hpp>
#include<conio.h> 

using namespace std;
using namespace cv;


template <class T>
int findValue(const cv::Mat& mat, T value) {
	int count = 0;
	for (int i = 0; i < mat.rows; i++) {
		const T* row = mat.ptr<T>(i);
		if (std::find(row, row + mat.cols, value) != row + mat.cols) { count++; }
	}
	return count;
}

int main()
{

	VideoCapture vid_capture("fast.mp4");

	int x = 50;
	int y = 50;
	int width = 100;
	int height = 100;
	int thickness = 2;

	Scalar lower_blue(94, 80, 2);
	Scalar upper_blue(120, 255, 255);

	Scalar lower_white(0,0,0);
	Scalar upper_white(0,0,255);

	Scalar lower_red(136, 87, 111);
	Scalar upper_red(180, 255, 255);



	if (!vid_capture.isOpened())
	{
		cout << "Error opening video stream or file" << endl;
	}

	else
	{
		int fps = vid_capture.get(5);
		cout << "Frames per second :" << fps;

		int frame_count = vid_capture.get(7);
		cout << "  Frame count :" << frame_count;
	}


	while (vid_capture.isOpened())
	{

		int key_arr = waitKeyEx(20);
		Rect rect(x, y, width, height);
		Mat frame, frame_copy,roi_image, roi_image_hsv;
		Mat mask_blue, mask_white, mask_red;
		Mat clean_blue;
		
		int count_blue, count_red, count_white;

		

		bool isSuccess = vid_capture.read(frame);

		frame.copyTo(frame_copy);

		if (isSuccess == true)
		{
			roi_image = frame_copy(rect);

			cvtColor(roi_image, roi_image_hsv, COLOR_BGR2HSV);

			inRange(roi_image_hsv, lower_blue, upper_blue, mask_blue);
			inRange(roi_image_hsv, lower_white, upper_white, mask_white);
			inRange(roi_image_hsv, lower_red, upper_red, mask_red);

			count_blue = findValue(mask_blue, Vec3b(255, 255, 255));
			count_red = findValue(mask_red, Vec3b(255, 255, 255));
			count_white = findValue(mask_white, Vec3b(255, 255, 255));

			if (count_blue > count_red && count_blue > count_white)
			{
				putText(frame, "Blue", Point(x + (width / 10), y + height - 20), FONT_HERSHEY_COMPLEX, 0.5, Scalar(0, 0, 255));
			}
			else
			{
				if (count_blue < count_red && count_red > count_white)
				{
					putText(frame, "Red", Point(x + (width / 10), y + height - 20), FONT_HERSHEY_COMPLEX, 0.5, Scalar(0, 0, 255));
				}
				else
				{
					if (count_blue < count_white && count_red < count_white)
					{
						putText(frame, "White", Point(x + (width / 10), y + height - 20), FONT_HERSHEY_COMPLEX, 0.5, Scalar(0, 0, 255));
					}
					else
					{
						putText(frame, "Unknown", Point(x + (width / 10), y + height - 20), FONT_HERSHEY_COMPLEX, 0.5, Scalar(0, 0, 255));
					}

				}

			}
			
			//cout << findValue(mask_white, Vec3b(255, 255, 255)) << endl;

			
			rectangle(frame, rect, cv::Scalar(0, 0, 255), thickness);
			imshow("Frame", frame);



			if (key_arr == 2424832) { x -= 10;}//left
			if (key_arr == 2555904) { x += 10; }//right 
			if (key_arr == 2490368) { y -= 10;}//up
			if (key_arr == 2621440) { y += 10; }//down
			if (key_arr == 27) { break; }
			
		}

	}
	vid_capture.release();
	destroyAllWindows();
	return 0;
}
