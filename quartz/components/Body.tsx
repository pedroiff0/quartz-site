import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import ThreeBackground from "./ThreeBackground"

const Body: QuartzComponent = ({ children }: QuartzComponentProps) => {
  return (
    <>
      <ThreeBackground />
      <div id="quartz-body">{children}</div>
    </>
  )
}

export default (() => Body) satisfies QuartzComponentConstructor
