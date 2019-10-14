var app = new Vue({
  el: "#app",
  data: {
    problems: [1, 2, 3, 4],
    currentProblem: 2,
    directions: {
      1: "Enter the letter a.",
      2: "Enter the letter b.",
      3: "Enter the letter c.",
      4: "Enter the letter d."
    },
    givens: {
      1: "",
      2: "",
      3: "",
      4: ""
    },
    solutions: {
      1: "a",
      2: "b",
      3: "c",
      4: "d"
    },
    correct:{
      1: false,
      2: false,
      3: false,
      4: false
    }
  },
  methods: {
    isComplete: function(problem) {
      return this.correct[problem];
    },
    log: function(event){
      console.log('Logging event.');
      fetch('./', {
        method: 'post',
        body: JSON.stringify(event)
      }).then(function(response) {
        return response.json();
      }).then(function(data) {
        console.log('logged event', data);
      });
    },
    check: function(){
      if (this.givens[this.currentProblem] === this.solutions[this.currentProblem]){
          this.correct[this.currentProblem] = true;
          this.log({"event":"correct"})
      } else {
          this.correct[this.currentProblem] = false;
          this.log({"event":"incorrect"})
      }
    }
  }
  
});