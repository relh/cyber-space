using UnityEngine;
using UnityEditor;
using System.Collections;

public class Move : MonoBehaviour {
	
	public float speed = 10.0F;
	public float rotationSpeed = 100.0F;
	public GameObject plane;
	Object site;

	int setToggle = 0;
	WWW set;

	// Use this for initialization
	void Start () {
		set = new WWW ("http://localhost:8080/retrieve?inputURL=neopets.com");
	}
	
	void Update() {
		float translate = 0;
		float xRotate = Input.GetAxis("Horizontal") * rotationSpeed;
		float yRotate = Input.GetAxis ("Vertical") * rotationSpeed;

		transform.Rotate (new Vector3(-yRotate*Time.deltaTime, xRotate*Time.deltaTime, 0), Space.Self);
		
		if (Input.GetButton("Fire2")) {
			translate = speed;
		}
		if (Input.GetButton ("Fire1")) {
			translate = -speed;
		}

		translate *= Time.deltaTime;
		transform.Translate (0, 0, translate);

		if (setToggle == 0 && set.isDone) {
			setToggle = 1;
			Debug.Log ("Set Loaded: " + set.url);
			AssetDatabase.Refresh();
			plane.GetComponent<Renderer>().material.mainTexture = (Texture)Resources.Load("webpage", typeof(Texture));
		}
	}


	void OnTriggerEnter(Collider other)
	{
		Debug.Log ("Collision: " + other.name);

		set = new WWW ("http://localhost:8080/retrieve?inputURL=" + other.name);

		setToggle = 0;

		//tex = Resources.Load("webpage") as Texture;
		//plane.renderer.material.mainTexture = tex;
	}
	
}
