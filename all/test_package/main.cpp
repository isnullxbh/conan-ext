#include <cassert>

#include <ext/result.hpp>

int main()
{
    ext::Result<int, int> r1 { ext::Success<int>(10) };
    const auto r2 = r1.map([](int v){ return v * 2; });
    assert(r2.value() == 20);
    return 0;
}
