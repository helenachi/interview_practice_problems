/* how are objects assigned/copied */
// a = {c:1}
// b = a
// console.log(a == b) // --> returns true


/* how are objects assigned/copied
   if an object is copied using the spread 
   operator, and one of the values is an object, 
   how is that copied? */
// function MyObject(x, y) {
//   this.x = x;
//   this.y = y;
//   this.o = null;
// }
// obj_one = new MyObject(1, 2)
// obj_one.o = new MyObject(3, 4)
// my_arr = ["4", 5, "ten", obj_one];
// arr_cp = [...my_arr];
// console.log(my_arr);
// console.log(arr_cp);


/* Convert a timestamp difference into a human 
readable format (i.e. "now", "a few seconds ago", 
"a few days ago") */
// console.log(+new Date);
// function readableTimeStamp(diff) {
//   if (diff < 5000) {
//     return "now";
//   } else if (diff < 30000) {
//     return "a few seconds ago";
//   } else if (diff < 300000) {
//     return "a few minutes ago";
//   } else if (diff < 86400000) {
//     return "a few hours ago";
//   } else {
//     return "a few days ago";
//   }
// }
// ctime = Date.now();
// setTimeout(() => console.log(readableTimeStamp(Date.now() - ctime)), 0);