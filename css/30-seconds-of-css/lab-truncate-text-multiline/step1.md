# Truncate Multiline Text

To truncate text that is longer than one line:

- Use `overflow: hidden` to prevent the text from overflowing its dimensions.
- Set a fixed `width` to ensure the element has at least one constant dimension.
- Set `height: 109.2px` for the container element, calculated from the `font-size`, using the formula `font-size * line-height * numberOfLines` (in this case `26 * 1.4 * 3 = 109.2`).
- Set `height: 36.4px` for the gradient container, calculated from the `font-size` and `line-height` using the formula `font-size * line-height` (in this case `26 * 1.4 = 36.4`).
- Use `background` with `linear-gradient()` to create a gradient from `transparent` to the `background-color`.

Add the following HTML code to implement the truncation:

```html
<p class="truncate-text-multiline">
  Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
  eirmod tempor invidunt ut labore et.
</p>
```

Use the following CSS code to style the container and gradient:

```css
.truncate-text-multiline {
  position: relative;
  overflow: hidden;
  display: block;
  height: 109.2px;
  margin: 0 auto;
  font-size: 26px;
  line-height: 1.4;
  width: 400px;
  background: #f5f6f9;
  color: #333;
}

.truncate-text-multiline::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 150px;
  height: 36.4px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #f5f6f9 50%);
}
```