import pyautogui, datetime, time


size = pyautogui.size()
print('Screen Size : {0}'.format(size))

while True:
    try:
        nowTime = datetime.datetime.now()
        # location = pyautogui.locateCenterOnScreen('skip.png', region = (1200, 750, 300, 100),
        #                                          confidence = 0.7)
        location = pyautogui.locateCenterOnScreen('skip.png', region = (0, 0, 1920, 1080),
                                                 confidence = 0.7)
    # region = (left, top, width, height)
    # you need to have OpenCV installed for the confidence keyword to word
        
        if location == None:
            print('[{0}] Ad not found. (Press "Ctrl + C" to quit)'.format(nowTime.strftime('%H:%M:%S')))
            time.sleep(2.0)
            
            continue
            
        print('[{0}] Ad not found at {1}.'.format(nowTime.strftime('%H:%M:%S'), location))
        pyautogui.moveTo(location[0], location[1], 1)
        pyautogui.click(button = 'left')
        time.sleep(5.0)
        
    except keyboardInterrupt:
        print('Thank you.')
        break


