#include <cstdint>
#include <iostream>
uint32_t f(int32_t v) {

  int32_t const mask = v >> 31;
  uint32_t r = (v + mask) ^ mask;
  return r;
}

int main() {
  std::cout << f(5) << std::endl;
  std::cout << f(0) << std::endl;
  std::cout << f(-5) << std::endl;
}
