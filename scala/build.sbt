scalaVersion := "2.11.8"

sparkVersion := "2.3.0"

spName := "eisber/sarplus"

version := "0.1.2" 

sparkComponents ++= Seq("core", "sql")

libraryDependencies ++= Seq(
  "commons-io" % "commons-io" % "2.6",
  "com.google.guava" % "guava" % "25.0-jre"
)

// All Spark Packages need a license
licenses := Seq("MIT" -> url("http://opensource.org/licenses/MIT"))

credentials += Credentials(Path.userHome / ".ivy2" / ".sbtcredentials") // A file containing credentials

spHomepage := "http://github.com/eisber/sarplus"

// If you published your package to Maven Central for this release (must be done prior to spPublish)
spIncludeMaven := true