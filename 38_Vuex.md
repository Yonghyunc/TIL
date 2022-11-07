# TIL

[Vuex](#vuex)

[Lifecycle Hooks](#lifecycle-hooks)

[Todo with Vuex](#todo-with-vuex)

<br><br>

---

# Vuex

## State Management (상태 관리)
▫ **State** : 현재에 대한 정보(data)   
▫ Web Application에서의 상태 표현 ➡ **현재 App이 가지고 있는 Data로 표현 O**   

▫ 우리는 여러 개의 component를 조합해서 하나의 App을 만들고 있음  
▫ 각 component는 **독립적**이기 때문에 각각의 상태(data)를 가짐  
▫ BUT 결국 이러한 component들이 모여서 하나의 App을 구성할 예정 ➡ 여러 개의 component가 같은 상태(data)를 유지할 필요가 있음  ➡ 상태 관리 필요 ‼   

<br>


### 🔹 Pass Props & Emit Event 상태 관리  
▫ 각 컴포넌트는 독립적으로 데이터 관리  
▫ 같은 데이터를 공유하고 있으므로, 각 컴포넌트가 동일한 상태를 유지하고 있음  
▫ 데이터 흐름 직관적으로 파악 가능  

❗ BUT 컴포넌트의 깊이가 깊어진다면 데이터 전달 구조가 복잡해짐  

<br>

### 🔹 Centralized Store 
▫ **중앙 저장소**에 데이터를 모아서 상태 관리  
▫ 각 component는 중앙 저장소의 데이터 사용  
▫ component의 **계층에 상관없이** 중앙 저장소에 접근하여 데이터 조회 및 변경 가능  
▫ 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터 반영      

<br><br>

## Vuex 
▫ "state management pattern + Library" for vue.js   
(상태 관리 패턴 + 라이브러리)   

▫ 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리  

▫ 데이터가 예측 가능한 방식으로만 변경될 수 있도록 하는 규칙을 설정하며, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능 제공  

<br><br>

➕ 플러그인 추가  
``` 
$ vue add vuex
```
▫ 파일트리에 store 폴더가 생성됨  

![image](https://user-images.githubusercontent.com/93974908/200209008-dff07c9c-8946-4402-8166-e9d650ff28c0.png)

<br>

### 🔹 vuex의 핵심 컨셉   
1. state
2. getters
3. mutations
4. actions


![image](https://user-images.githubusercontent.com/93974908/200209137-a5a7ccce-3668-4e97-88c4-da385937ffe2.png)

> data ➡ state  
> computed ➡ getters  
> methods ➡ mutations & actions (메서드의 역할에 따라 나뉨)  

<br><br>

### 1️⃣ State

▫ vue 인스턴스의 data   
▫ 중앙에서 관리하는 **모든 상태 정보**   
▫ 개별 component는  state에서 데이터를 가져와서 사용   
▫ state의 데이터가 변화하면 해당 데이터를 사용하는 component도 자동으로 다시 렌더링  
▫ `$store.state`로 state 데이터에 접근    

<br>

### 2️⃣ Mutations
▫ 실제로 **state를 변경**하는 유일한 방법  
▫ mutations 안의 함수 = 핸들러 함수 
▫ 핸들러 함수는 반드시 **동기적**이어야 함   
> 비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화 시기를 특정할 수 없음  

▫ 첫번째 인자 : `state`  
▫ component / Actions에서 `commit()` 메서드로 호출됨   

▫ commit(A, B)
- A : 호출하고자 하는 mutations 함수 
- B : payload 

<br>

### 3️⃣ Actions  
▫ mutations와 비슷하지만 **비동기 작업 포함 O**  
▫ state를 직접 변경하지 않고 commit() 메서드로 mutations를 호출해서 state 변경  

> state 변경 -> mutations  
> 그 외 나머지 -> actions 

▫ context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드 접근 가능  
> state 직접 변경 가능하지만, 하지 않아야 함 ‼

▫ component에서 `dispatch()` 메서드로 호출됨  

▫ dispatch(A, B)  
- A : 호출하고자 하는 actions 함수  
- B : 넘겨주는 데이터 (payload)

<br>

### 4️⃣ Getters  
▫ vue 인스턴스의 computed 에 해당   
▫ state를 활용하여 **계산된 값**을 얻고자 할 때 사용  
▫ state의 원본 데이터 영향 X  
▫ getters의 결과는 캐시되며, 종속된 값이 변경된 경우에만 재계산됨  
▫ 첫번째 인자 : `state`   
▫ 두번째 인자 : `getters`   

<br><br>

▫ vuex를 사용한다고 해서 모든 데이터를 state에 넣어야 하는 것은 아님   
▫ pass props & emit event 사용하여 상태 관리 O   
▫ 개발 환경에 따라 적절히 사용   

<br>

✔ 데이터 조작    
component ➡ Dispatch()를 통해 actions 호출 ➡ commit()을 통해 mutations 호출 ➡ state 변경  
> actions 생략 가능 

<br>

✔ 데이터 사용   
state ➡ getters ➡ component 
> getters 생략 가능  

<br><br>

## Vuex 실습 

▫ store의 state에 message 데이터 정의  
``` js
state: {
    message: 'message in store'
},
```
<br>

▫ component에서 state 직접 사용  (권장 X)  
``` html
<h1>{{ $store.state.message }}</h1>
```

<br>

▫ computed 에 정의 후 접근  
``` js
<template>
  <div id="app">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  computed: {
    message() {
      return this.$store.state.message
    }
  }
}
</script>
```
<br>

▫ 새로운 input 값으로 message 변경하기  
> actions에 정의된 changeMessage 함수에 데이터 전달  
> component에서 actions는 dispatch()에 의해 호출됨  
``` js
<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <input 
      type="text"
      @keyup.enter="changeMessage"
      v-model="inputData"
    >
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  components: {
  },
  computed: {
    message() {
      return this.$store.state.message
    }
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    }
  }
}
</script>
```
<br>

⭐ actions 
- 첫번째 인자 : context
- 두번째 인자 : payload 
``` js
actions: {
  changeMessage(context, newMessage) {
    console.log(context)
    console.log(newMessage)
  }
},
```
![image](https://user-images.githubusercontent.com/93974908/200212715-5d50ee7d-9f63-4e1f-97f2-24b618abf747.png)

> console.log(context)   
> context는 store의 전반적인 속성을 모두 가지고 있음  
> 모든 곳에 접근 가능, BUT 접근 안함 
> ![image](https://user-images.githubusercontent.com/93974908/200212741-bb5978a8-30cf-43e0-bd7d-51d3409d1633.png)

<br>

▫ 입력값으로 state 변경  
> actions에서 commit()을 통해 mutations 호출  
``` js
  mutations: {
    CHANGE_MESSAGE(state, newMessage) {
      state.message = newMessage
    }
  },
  actions: {
    changeMessage(context, newMessage) {
      context.commit('CHANGE_MESSAGE', newMessage)
    }
  },
```
> 이름 왜 대문자 ?  
> ➡ mutations 임을 강조하기 위하여 (actions와 구분)

> console.log(state)  
> ![image](https://user-images.githubusercontent.com/93974908/200214449-9a603e38-db5f-4487-9b30-d0789a72eb61.png)

> 사실상 action이 하는 일이 mutation 호출 밖에 없다면 사용하지 않아도 됨  

<br>

▫ state를 활용한 새로운 변수 messageLength (메세지의 길이 값)  
``` js
  getters: {
    messageLength(state) {
      return state.message.length
    }
  },
```
▫ getters 출력  
``` js
  computed: {
    ...
    messageLength() {
      return this.$store.getters.messageLength
    }
  },
```

<br><br>

---

# Lifecycle Hooks
▫ 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침  
- vue 인스턴스가 생성된 경우,
- 인스턴스를 DOM에 마운트하는 경우,
- 데이터가 변경되어 DOM을 업데이트하는 경우 등

▫ 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음 ➡ Lifestyle Hooks

<br>

![Lifecycle Hooks](https://vuejs.org/assets/lifecycle.16e4c08e.png)

<br><br>

1️⃣ created  
▫ vue 인스턴스가 생성된 후 호출  
▫ data computed 등의 설정이 완료된 상태  
▫ 서버에서 받은 데이터를 vue instance의 data에 할당하는 로직 구현 적합  
▫ BUT, mount되지 않아 요소 접근 X  

<br>

2️⃣ mounted   
▫ vue 인스턴스가 요소에 mount된 후 호출  
▫ mount된 요소 조작 O   

<br>

3️⃣ updated   
▫ 데이터가 변경되어 DOM에 변화를 줄 때 호출됨  


``` js
  created() {
    this.getDogImage()
    console.log('child created!')
  },
  mounted() {
    const button = document.querySelector('button')
    button.innerText = '멍멍!'
    console.log('child counted!')
  },
  updated() {
    console.log('새로운 멍멍이!')
    console.log('child updated!')
  }
```
![image](https://user-images.githubusercontent.com/93974908/200233220-c4b33dc7-77a4-454f-9414-ecf059bd9570.png)


<br><br>

### Lifecycle Hooks 특징 
▫ **인스턴스마다 각각의 Lifecycle을 가지고 있음**   
▫ Lifecycle Hooks는 컴포넌트별로 정의할 수 있음  
▫ 부모 컴포넌트의 mounted hook이 실행되었다고 해서 자식이 mount 된 것이 아니고, 부모 컴포넌트가 updated hook이 실행되었다고 해서 자식이 updated 된 것이 아님  
> 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않은 것  

<br><br>

---

# Todo with Vuex

구현 기능 
▫ Todo CRUD  
▫ Todo 개수 계산 
- 전체 Todo
- 완료된 Todo
- 미완료된 Todo

![image](https://user-images.githubusercontent.com/93974908/200234101-714c3e66-198a-40ec-aec9-9042df26883e.png)


<br><br>

### 사전 세팅 

``` 
$ vue create todo-vuex-app

$ cd todo-vuex-app

$ vue add vuex
```

▫ 컴포넌트 작성 
- TodoListItem.vue
- TodoList.vue
- TodoForm.vue
- App.vue

<br><br>

### Read Todo
▫ state 세팅   
``` js
  state: {
    todos: [
      {
        title: '할 일 1',
        isCompleted: false,
      },
      {
        title: '할 일 2',
        isCompleted: false,
      }
    ]
  },
```
<br>

▫ state 데이터 가져오기   

``` vue
// TodoList.vue

<template>
  <div>
    <TodoListItem
      v-for="(todo, index) in todos"
      :key="index"
      :todo="todo"
    />
  </div>
</template>

<script>
...
  computed: {
    todos() {
      return this.$store.state.todos
    }
  }
</script>
```
> 실제 프로젝트에서는 key값으로 배열의 각 요소 간 유일한 식별자 값을 사용 (생성시각 등)

<br>

▫ Pass Props 

``` vue
// TodoListItem.vue

<template>
  <div>{{ todo.title }}</div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  }
}
</script>
```

<br><br>

### Create Todo
▫ TodoForm    
> 입력 받을 input 태그 생성  
> todoTitle 정의  
> v-model로 양방향 바인딩  
> enter 이벤트로 createTodo 메서드  

``` vue
// TodoForm.vue

<template>
  <div>
    <input 
      type="text"
      v-model="todoTitle"
      @keyup.enter="createTodo"
    >
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      console.log(this.todoTitle)
    }
  }
}
</script>
```
<br>

▫ Actions   
> createTodo 메서드에서 actions 호출  

``` js
// TodoForm.vue

  methods: {
    createTodo() {
      this.$store.dispatch('createTodo', this.todoTitle)
      this.todoTitle = null
    }
  }
```
> actions에는 보통 비동기 관련 작업이 진행되지만, 현재 별도의 비동기 관련 작업이 불필요하기 때문에 todoTitle을 todo 객체로 만드는 과정 작성  

``` js
// index.js

  actions: {
    createTodo(context, todoTitle) {
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
    }
  },
```

<br>

▫ Mutations  

``` js
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      context.commit('CREATE_TODO', todoItem)
    }
  },
```
<br>

▫ 기존 더미 데이터 삭제  

``` js
state: {
  todos: [],
},
```

<br>

▫ 공백 문자가 입력되지 않도록 처리

- 좌우공백 X ➡  v-model.trim 

- 공백 입력 X  
    ``` js
    createTodo() {
        if (this.todoTitle) {
        this.$store.dispatch('createTodo', this.todoTitle)
        this.todoTitle = null
        }
    ```

<br><br>

### Delete Todo

▫ TodoListItem
> 삭제 버튼 + deleteTodo 메서드  

``` vue
<template>
  <div>
    {{ todo.title }}
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  }, 
  methods: {
    ...,
    deleteTodo() {
      this.$store.commit('DELETE_TODO', this.todo)
    }
  }
}
</script>
```
> 액션이 별다른 동작이 없는 경우 생략 가능 

``` js
  mutations: {
    ...,
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    }
  },
```

<br><br>

### Update Todo

▫ TodoListItem  
> todo를 클릭하면 완료 표시의 의미로 취소선 스타일 적용  
> 즉, todo의 isCompleted 값 토글  

``` vue
<template>
  <div>
    <span @click="updateTodoStatus">{{ todo.title }}</span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
...
  methods: {
    ...,
    updateTodoStatus() {
      this.$store.commit('UPDATE_TODO_STATUS', this.todo)
    }
  }
</script>
```

<br>

▫ Mutations

> todos 배열에서 선택된 todo의 isCompleted값만 토글한 후, 업데이트 된 todos 배열로 되어야 함 

> 반복을 돌면서 결과가 다시 todos로 할당  

``` js
UPDATE_TODO_STATUS(state, todoItem) {
    state.todos = state.todos.map((todo) => {
      if (todo === todoItem) {
        todo.isCompleted = !todo.isCompleted
      }
      return todo
    })
}
```

> 방법은 여러개  

``` js
UPDATE_TODO_STATUS(state, todoItem) {
    const index = state.todos.indexOf(todoItem)
    state.todos[index].isCompleted = !state.todos[index].isCompleted
}
```

<br>

▫ 취소선 스타일링  

> v-bind 활용해 isCompleted 값에 따라 css 클래스가 토글 방식으로 적용되도록 작성  

``` vue
<template>
  <div style="margin-bottom: 5px">
    <span 
      @click="updateTodoStatus"
      :class="{ 'is-completed': todo.isCompleted }"
    >
      {{ todo.title }}
    </span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<style>
  .is-completed {
    text-decoration:line-through;
  }
</style>
```

<br><br>

### 상태별 todo 개수 계산

▫ 전체 todo 개수   

``` js
// getters

allTodosCount(state) {
    return state.todos.length
}
```
``` js
// App.vue

  computed: {
    allTodosCount() {
      return this.$store.getters.allTodosCount
    },
  }
```

<br>

▫ 완료된 todo 개수  

``` js
// getters 

completedTodosCount(state) {
    const completedTodos = state.todos.filter((todo) => {
    return todo.isCompleted === true
    })
    return completedTodos.length
}
```

``` js
  computed: {
    ...,
    completedTodosCount() {
      return this.$store.getters.completedTodosCount
    }
  }
```

<br>

▫ 미완료 todo 개수  
=== 전체 개수 - 완료된 개수   
> getters는 두번째 인자로 getters를 받음  

``` js
  getters: {
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === true
      })
      return completedTodos.length
    },
    unCompletedTodosCount(state, getters) {
      return getters.allTodosCount - getters.completedTodosCount
    }
  },
```

![image](https://user-images.githubusercontent.com/93974908/200250501-00830ff6-6394-45be-babf-e8fc0cec54f9.png)

<br><br>

## Local Storage
▫ 브라우저의 Local Storage에 todo 데이터를 저장하여 브라우저를 종료하고 다시 실행해도 데이터가 보존될 수 있도록 함  

![image](https://user-images.githubusercontent.com/93974908/200251020-378b1905-43ef-496e-91f1-a3fe1203b53a.png)

<br>

### Window.localStorage
▫ 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨  
▫ 데이터가 문자열 형태로 저장됨  

< 메서드 >   
▫ setItem(key, value) : key - value 형태로 데이터 저장  
▫ getItem(key) : key에 해당하는 데이터 조회  

<br><br>

### 실습

▫ 데이터가 문자열로 저장되어야 하기 때문에 JSON.stringify를 통해 문자열로 변환해주는 과정 필요   
▫ actions에 작성  
> window는 생략 가능  ➡ localStorage.setItem()

``` js
saveTodosLocalStorage(context) {
    const jsonTodos = JSON.stringify(context.state.todos)
    localStorage.setItem('todos', jsonTodos)
}
```
<br>

▫ todo 생성, 삭제, 수정 시에 모두 saveTodosLocalStorage 메서드가 실행되도록 함  
``` js
  actions: {
    createTodo(context, todoTitle) {
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      context.commit('CREATE_TODO', todoItem)
      context.dispatch('saveTodosLocalStorage')
    },
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
      context.dispatch('saveTodosLocalStorage')
    },
    updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
      context.dispatch('saveTodosLocalStorage')
    },
    saveTodosLocalStorage(context) {
      const jsonTodos = JSON.stringify(context.state.todos)
      localStorage.setItem('todos', jsonTodos)
    }
  },
```

![image](https://user-images.githubusercontent.com/93974908/200253508-6b99c5d9-8ea7-4301-89a5-94bd6988de14.png)

<br>

BUT 새로고침 시 초기화됨  
➡ Local Storage로부터 데이터를 가져와야 함  

▫ 버튼을 누르면 불러오기
1. 불러오기 버튼 작성
    ``` js
    <button @click="loadTodos">Todo 불러오기</button>
    ```

2. load Todos 메서드 작성 
    ``` js
    methods: {
        loadTodos() {
        this.$store.dispatch('loadTodos')
        }
    }
    ```

3. load Todos action 메서드 작성
    ``` js
    actions: {
        ...,
        loadTodos(context) {
        context.commit('LOAD_TODOS')
        }
    },
    ```

4. LOAD_TODOS mutation 메서드 작성 
    - 문자열 데이터를 다시 object 타입으로 변환하여 저장 (JSON.parse)
    ``` js
    LOAD_TODOS(state) {
        const localStorageTodos = localStorage.getItem('todos')
        const parsedTodos = JSON.parse(localStorageTodos)
        state.todos = parsedTodos
    }
    ```

<br><br>

### vuex-persistedstate
▫ vuex state를 자동으로 브라우저의 Local Storage에 저장해주는 라이브러리 중 하나  
▫ 페이지가 새로고침 되어도 vuexx state를 유지시킴  
▫ Local Storage에 저장된 data를 자동으로 state로 불러옴   


``` 
$ npm i vuex-persistedstate
```

``` js
// index.js

import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  ...
})
```

