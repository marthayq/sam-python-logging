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
      2: true,
      3: false,
      4: true
    }
  },
  methods: {
    isComplete: function(problem) {
      return this.correct[problem];
    }
  }
  
});