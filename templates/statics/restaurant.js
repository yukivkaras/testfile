function good(){
    fetch('http://127.0.0.1:8080/')
    .then(res => res.text())
    .then(res => console.log(res))
  };

function goods(){
    var element = document.getElementById("aa").value;
    fetch('http://127.0.0.1:8080/a', {
        method: 'POST',
        mode: 'cors',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(element)
      })
    .then(res => res.text())
    .then(res => console.log(res))
  };