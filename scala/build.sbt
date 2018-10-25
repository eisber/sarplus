name := "sarplus"

organization := "eisber"

scalaVersion := "2.11.8"

sparkVersion := "2.3.0"

version := "0.1.1" 

sparkComponents ++= Seq("core", "sql")

libraryDependencies ++= Seq(
//  "org.apache.spark" %% "spark-core" % localSparkVersion,
// "org.apache.spark" %% "spark-sql" % localSparkVersion,
  "commons-io" % "commons-io" % "2.6",
  "com.google.guava" % "guava" % "25.0-jre"
)

spName := "eisber/sarplus"
