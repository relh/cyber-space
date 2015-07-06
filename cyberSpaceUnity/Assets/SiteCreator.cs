using UnityEngine;
using System;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.IO;

public class SiteCreator : MonoBehaviour 
{
	Dictionary<Tuple, Site> sites;

	void Start ()
	{
		sites = new Dictionary<Tuple, Site> ();

		TextAsset textAsset =(TextAsset)Resources.Load("dictionaryData");
		string result = textAsset.text;

		result = result.Substring (1, result.Length - 1);
		string pattern = @"\((\d+), (\d+)\): \((\d+), \'([A-Za-z0-9.]+)\'\), ";
		MatchCollection matches = Regex.Matches (result, pattern);;
		foreach (Match match in matches) {
			sites.Add(
				new Tuple(Convert.ToInt32(match.Groups[1].Value), Convert.ToInt32(match.Groups[2].Value)),
				new Site(Convert.ToInt32(match.Groups[3].Value), match.Groups[4].Value));
	
		}

		//Site none = sites[new Tuple(50, 50)];
		string comTLD = @"^[a-zA-Z0-9\-\.]+\.(com|COM)$";
		string eduTLD = @"^[a-zA-Z0-9\-\.]+\.(edu|EDU)$";
		string netTLD = @"^[a-zA-Z0-9\-\.]+\.(net|NET)$";
		string orgTLD = @"^[a-zA-Z0-9\-\.]+\.(org|ORG)$";
		string cnTLD = @"^[a-zA-Z0-9\-\.]+\.(cn|CN)$";
		string ruTLD = @"^[a-zA-Z0-9\-\.]+\.(ru|RU)$";
		string caTLD = @"^[a-zA-Z0-9\-\.]+\.(ca|CA)$";
		string jpTLD = @"^[a-zA-Z0-9\-\.]+\.(jp|JP)$";
		string inTLD = @"^[a-zA-Z0-9\-\.]+\.(in|IN)$";
		string deTLD = @"^[a-zA-Z0-9\-\.]+\.(de|DE)$";
		string itTLD = @"^[a-zA-Z0-9\-\.]+\.(it|IT)$";
		string frTLD = @"^[a-zA-Z0-9\-\.]+\.(fr|FR)$";
		string esTLD = @"^[a-zA-Z0-9\-\.]+\.(es|ES)$";

		foreach(var entry in sites)
		{
			// do something with entry.Value or entry.Key
			
			GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
			cube.transform.Translate(entry.Key.X*4, entry.Value.height/2, entry.Key.Y*4);
			cube.transform.localScale = new Vector3(1, entry.Value.height, 1);
			cube.GetComponent<Collider>().isTrigger = true;
			cube.GetComponent<Collider>().name = entry.Value.name;
			/*
			var tm = UnityEngine.GameObject.AddComponent(TextMesh);
			tm.text = entry.Value.name;
			tm.characterSize = 0.5f;
			*/

			if (Regex.IsMatch(entry.Value.name, comTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.cyan;
			} else if (Regex.IsMatch(entry.Value.name,eduTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.red;
			} else if (Regex.IsMatch(entry.Value.name,netTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.yellow;
			} else if (Regex.IsMatch(entry.Value.name, orgTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.blue;
			} else if (Regex.IsMatch(entry.Value.name,cnTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.magenta;
			} else if (Regex.IsMatch(entry.Value.name,ruTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.green;
			} else if (Regex.IsMatch(entry.Value.name, caTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.magenta;
			} else if (Regex.IsMatch(entry.Value.name,jpTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.magenta;
			} else if (Regex.IsMatch(entry.Value.name,inTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.green;
			} else if (Regex.IsMatch(entry.Value.name, deTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.blue;
			} else if (Regex.IsMatch(entry.Value.name,itTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.green;
			} else if (Regex.IsMatch(entry.Value.name,frTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.magenta;
			} else if (Regex.IsMatch(entry.Value.name, esTLD)) {
				cube.GetComponent<Renderer>().material.color = Color.red;
			}

		}
	}
}

//This is a safer, but slow, method of accessing
//values in a dictionary.
//if(sites.TryGetValue(new Tuple(40,40), out temp))
//{
//success!
//}
//else
//{
//failure!
//}