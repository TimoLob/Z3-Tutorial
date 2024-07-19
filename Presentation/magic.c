// Magic function
uint32_t f(int32_t v) {    
    int32_t const mask = v >> 31;
    uint32_t r = (v + mask) ^ mask;
    return r;
}