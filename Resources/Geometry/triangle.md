### Properties of a Triangle:

A **triangle** is a polygon with three sides, three vertices, and three angles. The basic properties of a triangle are as follows:

1. **Sum of Interior Angles**:
   - The sum of the interior angles of a triangle is always **180°**.
     \[
     \text{Angle 1} + \text{Angle 2} + \text{Angle 3} = 180^\circ
     \]

2. **Types of Triangles**:
   - **By Sides**:
     - **Equilateral Triangle**: All sides are equal, and all angles are 60°.
     - **Isosceles Triangle**: Two sides are equal, and the angles opposite those sides are also equal.
     - **Scalene Triangle**: All sides and angles are different.
   
   - **By Angles**:
     - **Acute Triangle**: All angles are less than 90°.
     - **Right Triangle**: One angle is exactly 90°.
     - **Obtuse Triangle**: One angle is greater than 90°.

3. **Triangle Inequality Theorem**:
   - The sum of the lengths of any two sides of a triangle must be greater than the length of the third side.
     \[
     a + b > c, \quad a + c > b, \quad b + c > a
     \]
     where \(a\), \(b\), and \(c\) are the sides of the triangle.

4. **Area of a Triangle**:
   - The area of a triangle can be calculated using various formulas:
     - **Base and Height**:
       \[
       \text{Area} = \frac{1}{2} \times \text{Base} \times \text{Height}
       \]
     - **Heron's Formula**: When all sides \(a\), \(b\), and \(c\) are known:
       \[
       \text{Area} = \sqrt{s(s - a)(s - b)(s - c)}
       \]
       where \(s = \frac{a + b + c}{2}\) (the semi-perimeter).

5. **Perimeter of a Triangle**:
   - The perimeter of a triangle is the sum of the lengths of its three sides:
     \[
     \text{Perimeter} = a + b + c
     \]

6. **Altitude**:
   - An altitude of a triangle is a perpendicular segment from a vertex to the line containing the opposite side. It is used to calculate the area and can vary depending on the type of triangle.

---

### Pythagorean Triplet:

A **Pythagorean triplet** is a set of three positive integers \(a\), \(b\), and \(c\) that satisfy the Pythagorean Theorem:
\[
a^2 + b^2 = c^2
\]
Where:
- \(a\) and \(b\) are the lengths of the legs of a right-angled triangle,
- \(c\) is the length of the hypotenuse (the side opposite the right angle).

#### Examples of Pythagorean Triplets:
- **(3, 4, 5)**: This is the most well-known triplet.
  \[
  3^2 + 4^2 = 9 + 16 = 25 = 5^2
  \]
- **(5, 12, 13)**:
  \[
  5^2 + 12^2 = 25 + 144 = 169 = 13^2
  \]
- **(7, 24, 25)**:
  \[
  7^2 + 24^2 = 49 + 576 = 625 = 25^2
  \]

#### Properties of Pythagorean Triplets:
1. **Primitive Triplets**: A Pythagorean triplet is called primitive if the greatest common divisor (GCD) of \(a\), \(b\), and \(c\) is 1. For example, (3, 4, 5) is a primitive triplet, but (6, 8, 10) is not, because the GCD is 2.
   
2. **Generating Pythagorean Triplets**:
   - Pythagorean triplets can be generated using two positive integers \(m\) and \(n\), where \(m > n\), using the formulas:
     \[
     a = m^2 - n^2, \quad b = 2mn, \quad c = m^2 + n^2
     \]
     For example, with \(m = 2\) and \(n = 1\):
     \[
     a = 2^2 - 1^2 = 3, \quad b = 2 \times 2 \times 1 = 4, \quad c = 2^2 + 1^2 = 5
     \]
     Hence, the triplet is (3, 4, 5).

3. **Multiplying a Pythagorean Triplet**:
   - Multiplying a Pythagorean triplet by a constant \(k\) results in another valid Pythagorean triplet. For instance, multiplying (3, 4, 5) by 2 gives (6, 8, 10), which is also a Pythagorean triplet.

Pythagorean triplets are used in geometry, trigonometry, and various practical applications involving right-angled triangles.