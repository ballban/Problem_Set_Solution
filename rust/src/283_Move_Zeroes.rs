struct Solution;

impl Solution {
  pub fn move_zeroes2(nums: &mut Vec<i32>) {
    let mut i = 0;
    let count = nums.len();
    for t in 0..count {
      if nums[i] == 0 {
        nums.remove(i);
        nums.push(0);
      } else {
        i += 1;
      }
    }
  }

  pub fn move_zeroes(nums: &mut Vec<i32>) {
    let mut i = 0;
    let count = nums.len();
    for t in 0..count {
      if nums[t] != 0 {
        nums[i] = nums[t];
        i += 1;
      }
    }
    for j in i..count {
      nums[j] = 0;
    }
  }
}

fn main() {
  let mut nums = vec![1,0,8,6,0,0,2,0,5,4,8,3,7];
  Solution::move_zeroes(&mut nums);
  println!("{:?}", nums);
}