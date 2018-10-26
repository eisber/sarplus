scalaVersion := "2.11.8"

sparkVersion := "2.3.0"

spName := "eisber/sarplus"

organization := "eisber"
name := "sarplus"

version := "0.2.2" 

sparkComponents ++= Seq("core", "sql")

libraryDependencies ++= Seq(
  "commons-io" % "commons-io" % "2.6",
  "com.google.guava" % "guava" % "25.0-jre",
  "org.scalatest" %% "scalatest" % "3.0.5" % "test",
  "org.scalamock" %% "scalamock" % "4.1.0" % "test"
)

// All Spark Packages need a license
licenses := Seq("MIT" -> url("http://opensource.org/licenses/MIT"))

// doesn't work anyway...
credentials += Credentials(Path.userHome / ".ivy2" / ".sbtcredentials") // A file containing credentials

spHomepage := "http://github.com/eisber/sarplus"

// If you published your package to Maven Central for this release (must be done prior to spPublish)
spIncludeMaven := true
