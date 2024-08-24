struct Solution;

impl Solution {
  pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
    let mut i = 0;
    let count = nums.len();
    for t in 0..count {
      if nums[t] != val {
        nums[i] = nums[t];
        i += 1;
      }
    }
    return i as i32
  }
}

fn main() {
  let mut nums = vec![1,0,8,6,0,0,2,0,5,4,8,3,7];
  Solution::remove_element(&mut nums, 0);
  println!("{:?}", nums);
}