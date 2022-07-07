import 'package:flutter/material.dart';
import 'dart:ui';

void main() {
  runApp(MaterialApp(home: MyApp()));
}

class MyApp extends StatefulWidget {
  MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  double? device_width;
  double? device_height;

  bool flag = true;

  @override
  Widget build(BuildContext context) {
    device_height =
        MediaQuery.of(context).size.height; //앱 화면 높이 double Ex> 692.0
    device_width = MediaQuery.of(context).size.width;

    print("작동하니? $device_width");

    Widget mix() {
      return Column(
        children: [
          // 프사
          profilePic(),
          // 캠핑사진
          campingPic(),
          //설명
          desc(),
          // 손톱이미지
          thumb(),
        ],
      );
    }

    return Scaffold(
      appBar: AppBar(
        title: Center(child: Text('실습')),
      ),
      body: ListView(
        padding: const EdgeInsets.all(8),
        children: <Widget>[
          mix(),
          mix(),
          mix(),
          mix(),
          mix(),mix(),mix(),mix(),mix(),mix(),mix(),mix(),mix(),

        ],
      ),
    );
  }

  Container thumb() {
    return Container(
      height: 100,
      color: Colors.blue,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Image.asset(
            'images/camping.jpg',
            width: 100,
            height: 70,
            fit: BoxFit.contain,
          ),
          Image.asset(
            'images/camping.jpg',
            width: 100,
            height: 70,
            fit: BoxFit.fill,
          ),
          Image.asset(
            'images/camping.jpg',
            width: 100,
            height: 70,
            fit: BoxFit.fill,
          ),
        ],
      ),
    );
  }

  Container desc() {
    return Container(
      decoration: BoxDecoration(
        border: Border.all(
          width: 5,
          color: Colors.orange,
        ),
      ),
      height: 100,
      child: Padding(
        padding: const EdgeInsets.only(left: 30, top: 20),
        child: Row(
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [Text("Number 10"), Text("Free camping")],
            ),
          ],
        ),
      ),
    );
  }

  Stack campingPic() {
    return Stack(
      children: [
        Image(image: AssetImage('images/camping.jpg')),
        Positioned(
          bottom: 10,
          width: device_width,
          child: Container(
            //color: Colors.red,
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  InkWell(
                    onTap: () {
                      setState(() {
                        flag = !flag;
                      });
                    },
                    child: flag
                        ? Icon(
                            Icons.heart_broken,
                            size: 50,
                            color: Colors.white,
                          )
                        : Icon(
                            Icons.heart_broken,
                            size: 50,
                            color: Colors.red,
                          ),
                  ),
                  Text(
                    "Let's Camping",
                    style: TextStyle(fontSize: 30, color: Colors.white),
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }

  Row profilePic() {
    return Row(
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: CircleAvatar(
            radius: 30.0,
            backgroundImage: AssetImage('images/face.jpg'),
          ),
        ),
        Text("내이름")
      ],
    );
  }
}
