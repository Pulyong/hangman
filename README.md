Hangman Game이란?
============
행맨게임의 규칙
------------
## 행맨
<img src="https://ww.namu.la/s/8da5aeb17af9030aa1ab5e384308b50aa7bf4067b055a45bfc24fed7806747fc27b439f8b8f131efd3b3628ca3d1054d6e81de2543beb7eb94e8ac0415e2c8b3c11a06248644206bc5b3d5daf5917202628034dbde6e1df081d0db97482f7782" width="250px" height="300px" title="Hangman" alt="Hangman"></img>
<p>
영어 단어 맞히기 게임 중 하나로, 글자 수만큼 빈칸 또는 밑줄을 그려놓고 26개 글자 중 하나를 대면 그 글자가 있을 경우 있는 칸에 있는 대로 다 적어놓고 없을 경우 라이프를 하나 깎는 게임. 
교수대에 교수형을 당하는 졸라맨 같은 사람의 그림을 그리는데, 처음에는 공백으로 시작하다가 한 글자 틀려서 라이프가 깎일 때 마다 그 틀린 글자를 표시해놓고 교수대-밧줄-머리-팔-손-몸통-다리-발 순서로 그어져서 
그림이 완성되면 지게 되는 게임이다. 일반적으로 10번의 기회가 있다.</p> 출처:나무위키


프로그램 코드
------------
### 1. 게임설정

* while문 안에서 input을 받아 원하는 단어를 입력합니다. 보통 행맨게임을 만들 때는 몇개의 단어를 미리 리스트에 입력해 둔 채 코드를 짜는데 저는 재미를 위해 원하는 만큼 단어를 입력할 수 있게 만들었습니다. 입력된 단어는 ask_list라는 리스트 안에 추가됩니다. 

* 단어 추가가 끝나면 "done!"을 입력해 while문을 빠져나옵니다.

* ask_list에 추가된 단어들 중 하나가 random함수를 이용해 무작위로 뽑아 ask라는 변수에 들어가게 됩니다. 그리고 원하는 만큼 life를 지정 할 수 있게 하였습니다.

### 2. 게임 진행

* while문의 조건을 life가 0이 되면 빠져나오게 만들었습니다.

* answer변수에 input으로 단어를 받아 letters변수에 추가됩니다. if문을 통해 기존에 letters변수에 있던 단어를 input받으면 다시 알파벳을 입력하라는 문구가 print되고, letters변수에 없던 알파벳들은 letters변수에 추가되고 정답,오답 문구가 print됩니다.

* for문에서 ask변수의 알파벳 하나하나를 가져와 if문에서 확인하여 ask에 letters에서 입력한 알파벳이 있으면 알파벳을, 없으면 "_"를 end=" "를 이용하여 한줄로 출력할 수 있게 만들었습니다.

* 한번이라도 "_"가 출력되면 succeed를 False로 설정하고 한번도 출력되지 않으면 succeed를 True로 유지하여 succeed가 True면 while문을 break할 수 있도록 만들었습니다.


후기
----

* 파이썬을 배우고 처음으로 조건문과 반복문, random함수등을 이용해 만든 프로그램입니다.

* 다양한 개념을 코드를 직접 만들어 봄으로써 어떤 식으로 개념이 쓰이는지 감을 잡을수 있었습니다.
