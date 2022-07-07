import 'package:flutter/material.dart';

// MediaQuery를 사용하여 기기의 weith와 height를 가져올 수 있다.

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: '실습'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(
          child: Text(widget.title),
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              padding: EdgeInsets.only(left: 10, top: 40, bottom: 20),
              child: Row(children: [
                CircleAvatar(
                  backgroundImage: AssetImage('assets/img.jpg'),
                  radius: 30,
                ),
                Text(' 내 이름', style: TextStyle(fontSize: 30)),
              ]),
            ),
            Column(
              children: [
                Stack(
                  children: [
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Image(image: AssetImage('assets/back.jpg')),
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Padding(
                          padding: const EdgeInsets.all(16.0),
                          child: Icon(Icons.favorite_border),
                        ),
                        Padding(
                          padding: const EdgeInsets.all(16.0),
                          child: Text('놀러갈 사람~'),
                        ),
                      ],
                    )
                  ],
                ),
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Container(
                    width: (MediaQuery.of(context).size.width),
                    height: 100,
                    decoration: BoxDecoration(
                      border: Border.all(
                        width: 1,
                        color: Colors.black
                      )
                    ),
                    child: Column(
                      children: [
                        Text('안녕. 나는 눈사람이야.'),
                        Text('너는 이름이 뭐니?')
                      ],
                    ),
                  ),
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}
