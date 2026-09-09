import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const ThreeBackground: QuartzComponent = ({ children }: QuartzComponentProps) => {
  return (
    <>
      <div
        id="three-bg-container"
        style="position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:-1;pointer-events:none;"
      ></div>
      {children}
    </>
  )
}

export default (() => ThreeBackground) satisfies QuartzComponentConstructor
