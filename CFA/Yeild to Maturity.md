The yeild-to-maturity is the **Internal Rate of Return** on a coupon paying bond, if you held the bond to maturity and all the coupons were re-invested as soon as they were received.

The bond typically has two cash flows:
    - Cashflow from coupon
    - Cashflow from repayment from principal

$$ PV(PMT) = \sum_{t=1}^{N} \frac{C}{(1+y)^t} $$

and


$$ PV(FV) = \frac{FV}{(1+y)^N} $$

Therefore, the total PV is:

$$ PV = \sum_{t=1}^{T} \frac{C}{(1+y)^t} + \frac{FV}{(1+y)^N} $$

Now solve for $y$ to get the yield from maturity. 

### Toy Example
Suppose:
| Bond Price | 1041 |
| FV | 1000 |
| Coupon Rate | 0.08 |
| Coupon Frequency | Annual |
| Maturity | 5y |

```cpp
double ytm (double price, double fv, double coupon_rate, double N) {
	double coupon = coupon_rate * fv;
	double return_per_year = (fv-price)/N;
	double average_value = (fv+pv)/2;
	return (coupon + return_per_year)/average_value;
}
```

It’s the **single discount rate** that makes the present value of **all future coupon + principal payments** equal to the bond’s current price.

#### YTM vs Reinvestment rate
- It’s the _actual rate_ you can earn on each coupon when you reinvest it in the real market.
## Price Yield Curve

We want
$$
PV(y)=\sum_{t=1}^{N}\frac{C}{(1+y)^t}+\frac{FV}{(1+y)^N}.
$$
For each coupon:
  $$
  \frac{d}{dy}\left(\frac{C}{(1+y)^t}\right) = -\frac{tC}{(1+y)^{t+1}}.
  $$
For principal:
  $$
  \frac{d}{dy}\left(\frac{FV}{(1+y)^N}\right) = -\frac{N FV}{(1+y)^{N+1}}.
  $$

---
$$
\frac{dPV}{dy} = -\sum_{t=1}^{N} \frac{tC}{(1+y)^{t+1}} - \frac{N FV}{(1+y)^{N+1}}.
$$

* Always **negative** ⇒ as yield (y) increases, bond price falls.
* Magnitude gives **sensitivity of price to yield** (basis for Macaulay/modified duration).

In fact,
$$
\frac{dPV}{dy} = -\frac{PV \cdot D_M}{1+y},
$$
where (D_M) = Macaulay duration.
