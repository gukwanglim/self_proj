// 모달 띄우기 코드

// modal이라는 상수를 만드는 코드입니다. 상수는 변하지 않는 값으로 한번 선언하면 그 뒤로 값을 바꿀 수 없습니다.
// https://cholol.tistory.com/552?category=739855
// const modal = document.getElementById("modal_add_feed");
// const modal_content = document.getElementById("modal_add_feed_content");

// // 앞으로 buttonAddFeed를 쓰면 우리가 만든 add_box 아이콘을 가리킵니다.
// const buttonAddFeed = document.getElementById("add_feed");

// // 이벤트 리스너(addEventListener)를 붙이면 buttonAddFedd에 무슨 일이 일어날 경우 괄호 안에 코드가 실행됩니다.
// // 코드는 modal의 style, 즉 CSS에서 display옵션을 "flex"로 바꿔준다는 의미입니다.
// buttonAddFeed.addEventListener("click", e => {

//     modal.style.top = window.pageYOffset + 'px'; // top을 이용해 시작 y위치를 바꿔줌. 즉, 현재 화면의 위치를 top이라고 설정하여 나오게 만든다. 
//                                             // 'px'를 포함해야지만 제대로 작동
//     modal_content.style.top = window.pageYOffset + 'px';

//     modal.style.display = "flex";
//     document.body.style.overflowY = "hidden"; // 스크롤 없애기

//     // 개발자 모드에서 로그 확인 가능. pageYOffset은 현재 화면에 y 위치를 알려준다.
//     console.log(window.pageYOffset + " 위치");    // 로그 찍기(화면이 내려간 상태에서 모달을 띄워도 상단에 고정되는 문제를 해결하기 위해)
// });



// jquery 부분

// 위 script 코드를 이런 식으로 jquery를 만들어서 사용할 수도 있음
$('#add_feed').click(function () {

    $('#modal_add_feed').css({
        top: window.pageYOffset + 'px',                  // 이런 식으로 넣어줘야 현재 내가 보고 있는 위치에 모달이 나옴
        display: 'flex'
    });

    // $('#modal_add_feed').css({
    //     display: 'flex'
    // });

    $(document.body).css({
        overflow: 'hidden'
    });

});


// 모달 닫기 코드
// const buttonCloseModal = document.getElementById("close_modal");
// buttonCloseModal.addEventListener("click", e => {
//     modal.style.display = "none";

//     document.body.style.overflowY = "visible";
// });



//위와 같이 사용해도 기능은 작동하지만 따로 함수를 만들면 더 편해진다.
$('.close_modal').on("click", () => {
    closeModal();
});

// $('#move_home').on("click",() =>{
//     $('#modal_add_feed_content').css({
//         top: window.pageYOffset + 'px',
//         display: 'flex'
//     });
//     $(document.body).css({
//         overflowY: "hidden"
//     });
// });

function closeModal() {
    $('.modal').css({
        display : 'none'
    });
    $(document.body).css({
        overflow : 'visible'
    });
};




// css에서 modal_image_upload 부분 가져오기
// class가 아닌 id로 찾아오는 법은 modal_image_upload에 id 값을 주고 $(#id명)을 하면 된다.(id를 사용할때는 '' 사용 안 함)
$('.modal_image_upload')
    // on()의 경우 자바스크립티의 addEventListener와 비슷(동작하는 방법)
    .on("dragover", dragOver)      // 마우스로 드래그해서 해당 div 위에 올리면 dragOver이라는 함수 실행
    .on("dragleave", dragOver)
    .on("drop", uploadFiles);      // 여기서 dragover나 dragleave, drop은 evnt의 type이 된다

    // on 안에(쉽게 말해 dragOver()의 형태가 아닌 dragOver만 사용) 함수를 호출할 때 아무것도 안 넣으면 event.data를 전달

// 이미지를 드래그했을 때 작동하는 함수
function dragOver(e){    // 여기서 e는 아무것이나 사용해도 상관없다

    console.log(e);                // 콘솔에서 log 확인

    e.stopPropagation();           // 전파 종료? 겹쳐져 있는 div 중에서 제일 상위에 있는 div만 클릭하게 하고 싶을 때
    e.preventDefault();            // 기본값 방지?
    
    if (e.type == "dragover") {
        $(e.target).css({
            "background-color": "black",
            "outline-offset": "-20px"
        });
    } else {
        $(e.target).css({
            "background-color": "white",
            "outline-offset": "-10px"
        });
    }
}


// 이미지를 drop 했을 때 작동하는 함수
let files;                              // function 밖에서 files를 let으로 정의했기 때문에 어디서든 files를 불러와서 사용할 수 있다.
function uploadFiles(e){

    // console.log(files)

    e.stopPropagation();
    e.preventDefault();

    //console.log(e.dataTransfer)                   // 내용 없음
    //console.log(e.originalEvent.dataTransfer)     // 내용 있음
    
    // 파일을 가져오는 부분(위까지는 프론트에서 파일을 읽어서 들고 있는 코드)
    e.dataTransfer = e.originalEvent.dataTransfer; 
    files =  e.dataTransfer.files;

    //console.log(files)        // 내용 들어옴
    //console.log(files[0])     // 확인 가능


    // 결론적으로는 files에 여러분이 드래그한 파일이 들어가게 됩니다
    // var files는 '리스트'형태

    if (files.length > 1) {
        alert('사진은 하나만 올려주세요.');

        $(e.target).css({
            "background-color": "white",
            "outline-offset": "-10px"
        });
        
        return;
    }

    $(e.target).css({
        "background-color": "white",
        "outline-offset": "-10px"
    });

    console.log(files[0].name)

    // 만약 올린 파일이 이미지가 아니면 경고
    // 혹은 올린 파일이 이미지가 맞다면 css에서 background로 지정 
    if (files[0].type.match(/image.*/)) {

        // 이 부분을 추가시킨 이유는?
        // {#$(e.target).css({#}
        //     {#    "background-image": "url(" + window.URL.createObjectURL(files[0]) + ")",#}
        //     {#    "outline": "none",#}
        //     {#    "background-size": "100% 100%"});#}


        $('#modal_add_feed_content').css({
            top: window.pageYOffset + 'px',
            display : 'flex'
        });

        $('.modal_image_upload_content').css({
            "background-image": "url(" + 'media/' + files[0].name + ")",
            "outline": "none",
            "background-size": "contain",
            "background-repeat" : "no-repeat",
            "background-position" : "center"
        });

        $('#modal_add_feed').css({
            display: 'none'
        })

        // $('#close_modal_2').on('click', ()=>{
        //     closeModal();
        // })

    }

    else{
        alert('이미지가 아닙니다.');
        return;
    }
}

// 이미지 업로드 이후 공유 버튼을 눌렀을 때

// $('#button_write_feed').on('click' 이 부분이 데이터를 긁어오는 부분
$('#button_write_feed').on('click', ()=>{
    const image = $('#input_image').css("background-image");
    const content = $('#input_content').val();
    const profile_image = $('#input_profile_image').attr('src');
    const user_id = $('#input_user_id').text();

    // image = $('#input_image').css("background-image");에는 /http://127.0.0.1:8000/fa24295d-469a-4be3-9a22-fbb280c7ff7f가 들어있다
    // image = $('#input_image').css("background-image").replace(/^url\(['"](.+)['"]\)/, '$1');에는 http://127.0.0.1:8000/ada2b5e0-771a-4329-ab68-ac3aab6fa8cd가 들어있다

    console.log(image)
    // console.log(content)
    // console.log(profile_image)
    // console.log(user_id)

    const file = files[0];


    let fd = new FormData();             // ajax에서 데이터를 서버로 받아오기 위해 FormData를 만들어 데이터를 저장해야한다.(쉽게 말해 데이터베이스에서 정보를 받아올 때 보여주는 형식과 같은 형식으로 만들어 준다고 생각하면 편하다.)

    fd.append('file', file);
    fd.append('image', image);
    fd.append('content', content);
    fd.append('profile_image', profile_image);
    fd.append('user_id', user_id);

    // console.log(fd.file)   // 내용 없음. append 가 되는 건가?

    if(image.length <= 0)
    {
        alert("이미지가 비어있습니다.");
    }
    else if(content.length <= 0)
    {
        alert("설명을 입력하세요");
    }
    else if(profile_image.length <= 0)
    {
        alert("프로필 이미지가 비어있습니다.");
    }
    else if(user_id.length <= 0)
    {
        alert("사용자 id가 없습니다.");
    }
    else{
        writeFeed(fd);
        console.log(files[0]);
    }
});

// 데이터를 서버로 전송하는 함수
function writeFeed(fd) {                 // ajax를 이용해 호출하여 fd라는 FormData를 넘김
    $.ajax({
        url: "/content/upload",          // 해당 경로의 views.py에 함수를 만들어 연결시켜야함(content/views.py에서 UploadFeed class 만들기) views.py에서 UploadFeed를 만들지 않으면 데이터베이스에 올라가지 않음.
        data: fd,
        method: "POST",
        processData: false,
        contentType: false,

        success: function (data) {
            console.log("성공");
            alert('업로드 완료!');
        },
        error: function (request, status, error) {
            console.log(fd);
            console.log("에러");
            alert('업로드 실패!');
        },
        complete: function() {           // complete는 성공이든 실패든 요청이 끝나면 무조건 실행
            console.log("무조건실행");    // 따라서 실패, 성공 여부를 따지지 않고 closeModal();을 사용해 modal 창 닫기.
            closeModal();                // 또한, 업로드한 feed를 메인화면에서 확인할 수 있도록 새로고침(location.reload();)
            location.reload();
        }
    })
};


// 회원가입 부분
$('#join_button').click(function () {

    // alert("회원가입 버튼을 누르셨습니다.");

    let email = $('#input_email').val();
    let password = $('#input_password').val();
    let nickname = $('#input_nickname').val();
    let name = $('#input_name').val();

    console.log(email, password, nickname, name);

    $.ajax({
        url: "/user/join",
        data: {
            email : email,
            password : password,
            nickname : nickname,
            name : name
        },
        method: "POST",
        success: function (data) {
            console.log("성공");
            alert("회원가입 성공했습니다. 로그인해주세요.");
            location.replace('/user/login');                     // 회원가입 성공 시 로그인 페이지로 이동

        },
        error: function (request, status, error) {
            alert("회원가입 실패했습니다. 정보를 정확히 기입해주세요.");
            console.log("에러");
        },
        complete: function () {
            console.log("완료");
        }
    });
});


// 로그인 부분
$('#login_button').click(function () {

    let email = $('#input_email').val();
    let password = $('#input_password').val();

    $.ajax({
        url: "/user/login",
        data: {
            email : email,
            password : password
        },
        method: "POST",
        success: function (data) {
            console.log("성공");
            alert("로그인 성공");
            location.replace('/');
        },
        error: function (request, status, error) {
            console.log("에러");
        },
        complete: function () {
            console.log("완료");
        }
    });
});

 
// 프로필 영역(내 게시물, 좋아요, 북마크를 눌렀을 때)                                        
$("#button_feed_list").click(function (){
    $('#feed_list').css({
        display : 'flex'
    });
    $('#like_feed_list').css({
        display : 'none'
    });
    $('#bookmark_feed_list').css({
        display : 'none'
    });
});
$("#button_feed_like_list").click(function (){
    $('#feed_list').css({
        display : 'none'
    });
    $('#like_feed_list').css({
        display : 'flex'
    });
    $('#bookmark_feed_list').css({
        display : 'none'
    });
});
$("#button_feed_bookmark_list").click(function (){
    $('#feed_list').css({
        display : 'none'
    });
    $('#like_feed_list').css({
        display : 'none'
    });
    $('#bookmark_feed_list').css({
        display : 'flex'
    });
});


                    //  이 부분은 499번 줄에서 email을 받아오는 법을 몰라서 html파일에 작성
// $('#button_profile_upload').click(function (){
//     $('#input_fileupload').click();
// });


// function profile_upload(){

//     let file = $('#input_fileupload')[0].files[0];
//     // console.log(file);

//     let email = "{{ user.email }}";
//     console.log(email);

//     let fd = new FormData();

//     fd.append('file', file);
//     fd.append('email', email);

//     $.ajax({
//         url: "/user/profile/upload",
//         data: fd,
//         method: "POST",
//         processData: false,
//         contentType: false,
//         success: function (data) {
//             console.log("성공");
//             alert('완료.');
//         },
//         error: function (request, status, error) {
//             console.log("에러");
//             alert('에러.');
//         },
//         complete: function () {
//             console.log("완료");
//             //location.replace("/content/profile");
//         }
//     });

// }

// 좋아요 누르기
$(".favorite").click(function (event) {
    let user = event.target.attributes.getNamedItem('user').value;
    console.log(user)

    if (user == 'None') {
        flag = confirm("로그인 하시겠습니까?")
        if (flag) {
          location.replace('/user/login')
        }
      } else {

        let feed_id = event.target.attributes.getNamedItem('feed_id').value;
        let favorite_id = event.target.id;

        console.log(feed_id);                                                      // 피드가 가진 고유한 id
        console.log(favorite_id);                                                  // 피드가 가진 고유한 id 앞에 favorite_을 붙인 id

        let favorite_text = $.trim($('#' + favorite_id).html());                   // 여기서 trim은 불필요한 공백을 없애주는 코드, favorite_id를 가진 아이콘을 눌렀을 때 그 아이콘의 이름을 반환.

        console.log(favorite_text);

        if (favorite_text == 'favorite') {                                         // 만약, 반환받은 아이콘이 비어있는 하트라면 하트를 채워서 반환
            $('#' + favorite_id).html('favorite_border');                          // (main.html에서는 단순하게 데이터베이스에 올라와있는 정보를 기반으로 색을 채운다.)
        } else {
            $('#' + favorite_id).html('favorite');
        }

        $.ajax({                                                                   // 좋아요를 눌렀을 경우, 그 정보를 데이터베이스에 반환.
            url: "/content/like",
            data: {
                feed_id: feed_id,
                favorite_text: favorite_text
            },
            method: "POST",
            success: function (data) {
                console.log("성공");
            },
            error: function (request, status, error) {
                console.log("에러");
            },
            complete: function () {
                console.log("완료");
            }
        });
    }
});

// 북마크 관련
$(".bookmark").click(function (event) {
    let user = event.target.attributes.getNamedItem('user').value;
    console.log(user)

    if (user == 'None') {
        flag = confirm("로그인 하시겠습니까?")
        if (flag) {
          location.replace('/user/login')
        }
      } else {

        let feed_id = event.target.attributes.getNamedItem('feed_id').value;
        let bookmark_id = event.target.id;
        let bookmark_text = $.trim($('#' + bookmark_id).html());
        if (bookmark_text == 'bookmark') {
            $('#' + bookmark_id).html('bookmark_border');
        } else {
            $('#' + bookmark_id).html('bookmark');
        }

        $.ajax({
            url: "/content/bookmark",
            data: {
                feed_id: feed_id,
                bookmark_text: bookmark_text
            },
            method: "POST",
            success: function (data) {
                console.log("성공");
            },
            error: function (request, status, error) {
                console.log("에러");
            },
            complete: function () {
                console.log("완료");
            }
        });
    }
});

