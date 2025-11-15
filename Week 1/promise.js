let myPromise = new Promise((resolve, reject) => {
  let success = true; // simulate condition

  if (success) {
    resolve("Task completed successfully!");
  } else {
    reject("Something went wrong!");
  }
});
myPromise.then(()=>{
    console.log("Success")
})
.catch(()=>{
    console.log("Fail")
})

