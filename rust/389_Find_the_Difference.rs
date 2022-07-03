struct Solution;

impl Solution {
  pub fn find_the_difference(mut s: String, t: String) -> char {
    for c in t.chars() {
      if !s.contains(c) {
        return c;
      }
      s.remove(s.find(c).unwrap());
    }
    return '0';
  }
}

fn main() {
  let s = String::from("abcd");
  let t = String::from("abcde");

  println!("{}", Solution::find_the_difference(s, t));
}