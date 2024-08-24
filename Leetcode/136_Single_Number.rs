struct Solution {
    a: i32
}
use std::collections::HashMap;

fn main() {
    let v = vec![4,1,2,1,2];
    // let x = Solution::new(1);
    // let y = Solution::new(2);
    // println!("{}", x.test());
    // println!("{}", y.test());
    // println!("{}", Solution::single_number(v));
    // println!("{}", Solution::test());
    println!("{}", Solution::single_number(v));
}

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut map = HashMap::new();
        for i in nums {
            *(map.entry(i).or_insert(0)) += 1;
        }
        for (key, value) in map {
            if value == 1 {
                return key;
            }
        }
        return 0;
    }
    pub fn new(num: i32) -> Solution{
        return Solution{
            a: num
        };
    }
    pub fn single_number2(nums: Vec<i32>) -> i32 {
        let mut re = 0;
        for i in nums {
            re = re ^ i;
        }
        return re;
    }
    pub fn test(&self) -> i32 {
        return self.a;
    }
}